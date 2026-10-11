import json
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from issues.models import Reporter, Issue, CriticalIssue, LowPriorityIssue

REPORTERS_FILE = 'reporters.json'
ISSUES_FILE = 'issues.json'

def load_data(file_path):
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []

def save_data(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)


@csrf_exempt
def reporters_view(request):
    if request.method == 'GET':
        reporters = load_data(REPORTERS_FILE)
        reporter_id = request.GET.get('id')
        if reporter_id is not None:
            for rep in reporters:
                if rep['id'] == int(reporter_id):
                    return JsonResponse(rep, status=200)
            return JsonResponse({'error': 'Reporter not found'}, status=404)
        return JsonResponse(reporters, safe=False, status=200)

    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            reporter = Reporter(
                id=data.get('id'),
                name=data.get('name'),
                email=data.get('email'),
                team=data.get('team')
            )
            reporter.validate()

            reporters = load_data(REPORTERS_FILE)
            reporters.append(reporter.to_dict())
            save_data(REPORTERS_FILE, reporters)

            return JsonResponse(reporter.to_dict(), status=201)
        except ValueError as e:
            return JsonResponse({'error': str(e)}, status=400)
        except Exception as e:
            return JsonResponse({'error': 'Invalid request data'}, status=400)

    return JsonResponse({'error': 'Method not allowed'}, status=405)


@csrf_exempt
def issues_view(request):
    if request.method == 'GET':
        issues = load_data(ISSUES_FILE)
        issue_id = request.GET.get('id')
        status = request.GET.get('status')

        if issue_id is not None:
            for item in issues:
                if item['id'] == int(issue_id):
                    return JsonResponse(item, status=200)
            return JsonResponse({'error': 'Issue not found'}, status=404)

        if status is not None:
            filtered = [item for item in issues if item['status'] == status]
            return JsonResponse(filtered, safe=False, status=200)

        return JsonResponse(issues, safe=False, status=200)

    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            priority = data.get('priority')

            # Polymorphism: Pick subclass based on priority
            if priority == 'critical':
                issue = CriticalIssue(
                    data.get('id'), data.get('title'), data.get('description'),
                    data.get('status'), priority, data.get('reporter_id')
                )
            elif priority == 'low':
                issue = LowPriorityIssue(
                    data.get('id'), data.get('title'), data.get('description'),
                    data.get('status'), priority, data.get('reporter_id')
                )
            else:
                issue = Issue(
                    data.get('id'), data.get('title'), data.get('description'),
                    data.get('status'), priority, data.get('reporter_id')
                )

            issue.validate()

            response_data = issue.to_dict()
            response_data['message'] = issue.describe()

            issues = load_data(ISSUES_FILE)
            issues.append(response_data)
            save_data(ISSUES_FILE, issues)

            return JsonResponse(response_data, status=201)
        except ValueError as e:
            return JsonResponse({'error': str(e)}, status=400)
        except Exception:
            return JsonResponse({'error': 'Invalid request data'}, status=400)

    return JsonResponse({'error': 'Method not allowed'}, status=405)

from datetime import datetime, timedelta


def fetch_commit_details(commits_JSON):
    commits_details_lst = []
  
    for commit in commits_JSON:
        commit_row = {}
        commit_row['user_id'] = commit['author']['id']
        commit_row['DATE'] = [commit['commit']['author']['date']]
        commit_row['Message'] = commit['commit']['message']
        commit_row['comment_count'] = commit['commit']['comment_count']
        commits_details_lst.append(commit_row)
       
    return commits_details_lst

def fetch_event_details(events_JSON):
    event_details_lst = []

    for event in events_JSON:
        event_row = {}
        event_row['event_id'] = event['id']
        event_row['event'] = event['event']
        event_row['created_at'] = event['issue']['created_at']
        event_row['closed_at'] = event['issue']['closed_at']
        event_row['comments'] = event['issue']['comments']

        event_details_lst.append(event_row)
    return event_details_lst



def filter_json(json, keys):
    '''
        A function to Filter only several keys from a JSON
    '''
    return {key: json[key] for key in keys}
    
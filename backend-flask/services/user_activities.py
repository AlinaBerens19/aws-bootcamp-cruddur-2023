import os
from datetime import datetime, timedelta, timezone
# Import XRay SDK libraries
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware

class UserActivities:
    def __init__(self, request):
        self.request = request

    def run(self, user_handle):
        model = {
            'errors': None,
            'data': None
        }
        try:
            # Start a parent subsegment
            parent_subsegment = xray_recorder.begin_subsegment('user_activities_start')
            parent_subsegment.put_annotation('url', self.request.url)

            now = datetime.now(timezone.utc).astimezone()
            xray_dict = {'now': now.isoformat()}
            parent_subsegment.put_metadata('now', xray_dict, 'user_activities')
            parent_subsegment.put_metadata('method', self.request.method, 'http')
            parent_subsegment.put_metadata('url', self.request.url, 'http')

            if user_handle is None or len(user_handle) < 1:
                model['errors'] = ['blank_user_handle']
            else:
                try:
                    # Start a nested subsegment
                    subsegment = xray_recorder.begin_subsegment('user_activities_nested_subsegment')
                    now = datetime.now()
                    results = [{
                        'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
                        'handle':  'Andrew Brown',
                        'message': 'Cloud is fun!',
                        'created_at': (now - timedelta(days=1)).isoformat(),
                        'expires_at': (now + timedelta(days=31)).isoformat()
                    }]
                    model['data'] = results
                    xray_dict['results'] = len(model['data'])
                    subsegment.put_metadata('results', xray_dict, 'user_activities')
                except Exception as e:
                    subsegment.put_annotation('error', str(e))  # Add error info to the subsegment
                    raise e
                finally:
                    xray_recorder.end_subsegment()
        except Exception as e:
            parent_subsegment.put_annotation('error', str(e))  # Log the error in the parent subsegment
            model['errors'] = [str(e)]
        finally:
            # Ensure the parent subsegment is closed
            xray_recorder.end_subsegment()

        return model

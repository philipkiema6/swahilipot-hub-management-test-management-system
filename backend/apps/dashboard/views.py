from django.apps import apps
from rest_framework import permissions,response,views
def safe_count(a,m):
 try: return apps.get_model(a,m).objects.count()
 except Exception: return 0
class DashboardSummaryView(views.APIView):
 permission_classes=[permissions.IsAuthenticated]
 def get(self,request): return response.Response({'kpis':[
  {'key':'equipment','label':'Equipment Management','value':safe_count('equipment','Equipment')},
  {'key':'projects','label':'Project Submission','value':safe_count('projects','ProjectSubmission')},
  {'key':'subscriptions','label':'Software Subscriptions','value':safe_count('subscriptions','SoftwareSubscription')},
  {'key':'wifi','label':'Wi-Fi Access Management','value':safe_count('wifi','WifiAccessRequest')},
  {'key':'feedback','label':'Feedback & Complaints','value':safe_count('feedback','Ticket')},
  {'key':'filetransfer','label':'File Transfer System','value':safe_count('filetransfer','FileTransfer')},
  {'key':'fmreport','label':'FM Station Monitoring','value':safe_count('fmreport','FMStatusReport')},
  {'key':'calls','label':'Call Recording Management','value':safe_count('calls','CallRecording')},
  {'key':'radio','label':'Radio Scheduling','value':safe_count('radio','RadioShow')},
  {'key':'news','label':'News CMS','value':safe_count('news','Article')},
  {'key':'videography','label':'Videography Management','value':safe_count('videography','ShootRequest')},
 ]})

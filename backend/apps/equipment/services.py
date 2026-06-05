import csv
from django.http import HttpResponse
def export_csv(qs):
 r=HttpResponse(content_type='text/csv'); r['Content-Disposition']='attachment; filename=equipment.csv'; w=csv.writer(r); fields=[f.name for f in qs.model._meta.fields]; w.writerow(fields); [w.writerow([getattr(o,f) for f in fields]) for o in qs]; return r

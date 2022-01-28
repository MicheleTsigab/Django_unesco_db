import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Site, Category, State,Iso,Region

def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header
    Site.objects.all().delete()
    Category.objects.all().delete()
    State.objects.all().delete()
    Iso.objects.all().delete()
    Region.objects.all().delete()
    # Format
    # email,role,course
    # jane@tsugi.org,I,Python
    # ed@tsugi.org,L,Python

    for row in reader:
        print(row)
        ca, created = Category.objects.get_or_create(name=row[7])
        r, created = Region.objects.get_or_create(name=row[9])
        st,created=State.objects.get_or_create(name=row[8],region=r)
        i,created=Iso.objects.get_or_create(name=row[10])
        try:
            y = int(row[3])
            a=float(row[6])
        except:
            y = None
            a=None
        s=Site(name=row[0],description=row[1],justification=row[2],year=y,longitude=row[4],latitude=row[5],area_hectares=a,category=ca,state=st,iso=i)
        s.save()
        #r = Membership.LEARNER
        #if row[1] == 'I':
         #   r = Membership.INSTRUCTOR
        #m = Membership(role=r, person=p, course=c)
        #m.save()
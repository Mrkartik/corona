import COVID19Py
kt=COVID19Py.COVID19()
def show(x):
    cd=x
    code=kt.getLocationByCountryCode(cd)
    ld=code[0]
    vd=dict(ld['latest'])
    print("Country Name = "+ld['country']+","+ld['country_code']+"\n")
    print("Country Population = "+str(ld['country_population'])+"\n")
    print("Confirmed = "+str(vd['confirmed'])+"\n")
    print("Deaths = "+str(vd['deaths'])+"\n")
    lu=ld['last_updated']
    print("Last Updated = "+lu[0:10]+"\n")


print("First Find Country code by going to this link \n https://www.willmaster.com/blog/misc/country-name-abbreviations.php ")
print("Enter Country Name: \n Eg:- India = In \n united States = Us \n United Kingdom = Gb \n")
x=input()
show(x)

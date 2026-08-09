import requests

while True:
    name = input("what is the compound?")
    try:
        response = requests.get(
        f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{name}/property/MolecularFormula,MolecularWeight,CanonicalSMILES,IUPACName/JSON")
        data = response.json()
        ptable = data["PropertyTable"]
        properties = ptable.get("Properties")
        important = properties[0]
        print(important.get("MolecularFormula"))
        print(important.get("MolecularWeight"))
        print(important.get("ConnectivitySMILES"))
        print(important.get("IUPACName"))
        break
    except KeyError:
        print("pls write again")
        continue
    except requests.exceptions.RequestException:
        print("weak internet connection")
        continue

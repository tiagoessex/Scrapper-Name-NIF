
Version: 0.0.1

# Description

* Given an entity's name and/or nif, tries to retrieve information about that entity from 6 sites. It returns a json with all the available information.
* The program will scrap all _6_ sites, if possible, and the resulting json, will be the resulting merging of the results from all sites.
* In case nothing is found (maybe the entity doesn't exist), *'status': 'NOT FOUNDED'*, else *'status': 'OK'*.


# Requirements

* Python 3.7.x


# Fields

* type
* nome
* nome_legal
* nif
* data_de_inicio
* morada
* localidade
* distrito
* concelho
* freguesia
* codigo_freguesia
* codigo_postal
* forma_juridica
* telefone
* fax
* cae
* site
* latitude
* longitude
* horario
* email
* telemovel
* estado
* status
* url


# Sites
* [https://www.racius.com/](https://www.racius.com/)
* [https://codigopostal.ciberforma.pt/](https://codigopostal.ciberforma.pt/)
* [https://www.portugalio.com/](https://www.portugalio.com/)
* [https://www.gescontact.pt/](https://www.gescontact.pt/)
* [https://www.einforma.pt/](https://www.einforma.pt/)
* [https://guiaempresas.universia.pt/](https://guiaempresas.universia.pt/)


# Example

```python
import scraping

# True => randomize the order of the services
s = Scrapping(True)	
r = s.scrap("Ideias Bring Solutions Lda")
print (r)

print ("---------------")
r = s.scrap("HEMOVIDA Lda", 506036944)
print (r)
```


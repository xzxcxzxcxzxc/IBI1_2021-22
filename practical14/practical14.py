from xml.dom.minidom import parse 
import xml.dom.minidom
import matplotlib.pyplot as plt

def recursion(term,e):
    global terms
    global g
    is_as = term.getElementsByTagName('is_a')
    for is_a in is_as:
        c = is_a.childNodes[0].data
        if g[c] == {c:0}:
            e.append(c)
            for i in e:
                g[i][c] = 0
            recursion(terms[list(g.keys()).index(c)],e)
            del e[-1]
        else:
            for i in e:
                g[i].update(g[c])


domtree = xml.dom.minidom.parse("go_obo.xml")
collection = domtree.documentElement
terms = collection.getElementsByTagName("term")
g = {}
a = {}
f = []
b = []

for term in terms:
    name = term.getElementsByTagName('id')[0].childNodes[0].data
    g[name] = {name:0}
    a[name] = -1

for term in terms:
    e = [term.getElementsByTagName('id')[0].childNodes[0].data]
    recursion(term,e)

for i in g.values():
    for j in i:
        a[j] += 1

for term in terms:
    if 'translation' in term.getElementsByTagName('defstr')[0].childNodes[0].data.lower():
       f.append(a[term.getElementsByTagName('id')[0].childNodes[0].data])

print('there are ',len(g.keys()),'terms in the Gene Ontology')
print('the average childnodes is',sum(a.values())/len(g.keys()))
print('the average childnodes of translation term is',sum(f)/len(f))
print('so it means that translation term have more childnodes than average')

plt.subplot(121)
plt.boxplot(a.values())
plt.title('Distribution of child node number of all GO terms')
plt.xlabel("all GO terms")
plt.ylabel("Number")
plt.subplot(122)
plt.boxplot(f)
plt.title('Distribution of child node number of terms associated with ‘translation’')
plt.xlabel("associated with ‘translation’")
plt.ylabel("Number")
plt.show()


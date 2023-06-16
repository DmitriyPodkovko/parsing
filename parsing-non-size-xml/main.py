from io import StringIO
from lxml import etree, objectify
import pickle


document = """\
<slideshow>
<title>Demo slideshow</title>
<slide>
    <title>Slide title</title>
    <point>This is a demo</point>
    <point>Of a program for processing slides</point>
</slide>

<slide>
    <title>Another demo slide</title>
    <point>It is important</point>
    <point>To have more than</point>
    <point>one slide</point>
</slide>
</slideshow>
"""

class Holder:
    def __setattr__(self, name, value):
        new_name = name
        i = 1
        while hasattr(self, new_name):
            new_name = name + str(i)
            i += 1
        return super().__setattr__(new_name, value)


tree = objectify.parse(StringIO(document))
root = tree.getroot()

def compile_xml(data_object, local_root):
    for child in local_root.iterchildren():
        if child.countchildren()==0:
            setattr(data_object, child.tag, child.text)
        else:
            node_obj = compile_xml(Holder(), child)
            setattr(data_object, child.tag, node_obj)
    return data_object

data_object = Holder()
res = compile_xml(data_object, root)
print(dir(res))

s = pickle.dumps(res)
print(s)

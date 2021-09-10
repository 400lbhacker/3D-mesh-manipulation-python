# 3D-mesh-manipulation-python
3D mesh manipulation via python

their are several libraries available that let you render a 3D object easily, however that was not enough. I needed the ability to physically edit/modify the meshes. I have been working on something similear to http://endlessforms.com/ 

I have tried pymesh, pymesh2, trimesh, and several other libraries that have failed. I have tried both python 2 & python 3 libraries both new and old none worked. the following python file example I have above despite being relatively short, is a very powerful succesful example. I am using the open3D library, I suggest you read their introduction here: http://www.open3d.org/docs/release/introduction.html for more details. I had trouble getting most of their tutorial snippets to work, and when i got one working was having issues combining it with other examples but was able to finally create my own that did work. my file above ~ It performs the following abilities:

can take any mesh file (.obj, .stl etc) and export it as another
can reduce the number of vertices or increase them (in this case I was able to take a simple tesselated teapot .obj and create a much higher quality virtually smooth version of it)
can perform functions to deform the mesh (in this case a rotation function on the y axis)
can convert the 3d model into a point cloud composed of vorxels 
automatically creates a .obj and .jpg for each function result and saves them in directory

here is a following example, the first img being the initial unmodified original teapot .obj
![A test image1](https://i.ibb.co/VMYgGQ1/240742906-110691848004026-7463177260577898412-n.jpg)

I am looking to team up with other researchers, professionals, or bored jobless python enthusiast like myself to create a python code to perform hybridization of two models using python, genetic algorythems in python, signal processing or conv/relu/guascian/laplace (etc), CPPN & MD-HYPERNEAT like functions on a model using python, and many other things to create us a endlessforms-like engine, I do beleive we can get it down to a single .py file

one last thing. Is this code is EXTREMELY performance efficient. Was able to easily modify a massive 21,000+ vertices, 20 mb+ .OBJ file of an entire MI-24 helicopter and perform amazing functions with it in just a couple seconds (NO GPU) just simply using cpu on a 4gb ram laptop. 

please feel free to contact me via the following

facebook: https://www.facebook.com/profile.php?id=100071896345565

gmail: josepherickson135@gmail.com

enjoy.



 

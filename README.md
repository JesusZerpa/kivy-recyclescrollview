# kivy-recyclescrollview
Este proyecto se trata de un widget construido mediante un script para crear una caja de scroll desde la cual se pueda ingresar muchos widgets incluso widgets personalizados creados por el usuario, sin consumir un exeso de memoria y de facil implementacion. 

Contrui este script dado que la documentacion que encontre del RecycleView que encontre de Kivy indicaba que el modulo es experimental y al momento de probarlo no pude usarlo con mis widgets personalizados no funciono, entonces opte por crear yo este tipo de widget y hasta el momento me a parecido funcionar como queria

Nota: para usar los modulos personalizados dentro de RecycleScrollView necesitara registrar su widget en la factory de Kivy ejemplo:
<code>
#widget personalizado

class Found(BoxLayout):
	pass

Factory.register("Found",cls=Found)
</code>
ahora utilize el lenguaje kv para construir la representacion grafica que necesita:
<code>
<Found>:
	size_hint: (1, None)
	max_height: 200	
	orientation: 'horizontal'
	text:StringProperty("")
	on_text:
		
		root.ids["title"].text=args[1]
	Image:
		source: "imgs/carousel/slide1.jpg"
	BoxLayout:
		orientation: 'vertical'
		Label:
			id:title
			text:"hola"
			color:0,0,0,1
		Label:
			text:"mundo"
			color:0,0,0,1
<Root>:
  BoxLayout:
    viewclass:"Found"#clase del widget
    data:[{"text":f"boton {x}"} for x in range(100000000)]#datos a renderizar
</code>


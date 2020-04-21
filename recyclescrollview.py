from kivy.factory import Factory
from kivy.properties import *
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout

class RecycleScrollView(Factory.ScrollView):
	viewclass=StringProperty("")
	data=ListProperty([])
	#box
	orientation= 'vertical'
	
	default_height= 1000
	cursor=0
	max_items=10
	widget_height=None
	def __init__(self,*args,**kwargs):
		super(RecycleScrollView,self).__init__(*args,**kwargs)		
		self.do_scroll_y=True
		self.box=BoxLayout(orientation="vertical",size_hint_y= None,height=self.default_height)
		self.add_widget(self.box)


		
	
		
	
	def on_parent(self,instance,value):
		pass
	def on_size(self,instance,value):
		height=0
		for elem in self.children[0].children:
			height+=elem.height
		
		self.children[0].height=height
	def on_scroll_move(self,instance):
		
		if self.widget_height:
			
			dx=self.box.height-(self.scroll_y*self.box.height)
			if dx>0:

				item_passed=dx/self.widget_height

				self.cursor=int(item_passed)
			
			self.update()
		return super().on_scroll_move(instance)
	def on_scroll_stop(self,instance):
		
		if self.widget_height:
			
			dx=self.box.height-(self.scroll_y*self.box.height)
			if dx>0:

				item_passed=dx/self.widget_height

				self.cursor=int(item_passed)
			
			self.update()
		return super().on_scroll_stop(instance)
	
	def update(self):

		self.clear_widgets()
		widget=getattr(Factory,self.viewclass)
		_widget=widget()

		self.box=FloatLayout(size_hint_y= None,height=self.default_height)
		
		super(RecycleScrollView,self).add_widget(self.box)
		
		self.box.top=self.top
		


		for k,item in enumerate(self.data[self.cursor:self.cursor+self.max_items]):
			widget=getattr(Factory,self.viewclass)
			_widget=widget()
			_widget.size_hint_y=None
			self.box.add_widget(_widget)
			_widget.pos=(_widget.pos[0],(_widget.height*len(self.data))-(_widget.height*(self.cursor+k+1)))
			for elem in item:
				setattr(_widget,elem,item[elem])
			
			
		self.box.height=self.widget_height*len(self.data)


			


			
		



	def on_classview(self,instance,value):
		instance.classview=value
		

	def on_data(self,instance,value):
		
		#button
		#size_hint: (1, None)
		#height: 200
		self.data=value
		for k,item in enumerate(self.data[self.cursor:self.cursor+self.max_items]):
			widget=getattr(Factory,self.viewclass)
			_widget=widget()
			_widget.size_hint_y=None
			for elem in item:
				setattr(_widget,elem,item[elem])
			if self.widget_height==None:
				self.widget_height=_widget.height
			self.box.add_widget(_widget)
		




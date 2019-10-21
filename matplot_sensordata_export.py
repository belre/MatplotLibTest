
# Copyright (c) 2012-2013 Matplotlib Development Team
# All Rights Reserved

# * Install pillow to use pip or pip3 before executing

from PIL import Image
import matplotlib.pyplot as plt

class CMatplotLibController:
	def Initialize(self):
		import matplotlib
		matplotlib.use('Agg')
	
	def InitCommonParams(self):
		self._int_params = {
					'xlabel': 'Channel',
					'ylabel': 'Intensity',
					'xlim' : [0, 80],
					'ylim' : [0, 256],
					'isgrid' : True,
					'fontsize_label' : 16,
					'margin_top' : 0.95,
					'margin_bottom' : 0.12,
					'margin_right' : 0.95,
					'margin_left' : 0.12
					}
	
	
	def SetManualCommonParams(self, int_params):
		self._int_params = int_params
	
	
	def ExportGraph(self, data_Xp, data_Yp):
		plt.clf()
		plt.tight_layout()
		fig = plt.figure(1)
		ax = fig.add_subplot(1,1,1)
		ax.plot(data_Xp, data_Yp, marker='o', linestyle='None')
		
		fontsize_label = 12
		if 'fontsize_label' in self._int_params:
			fontsize_label = self._int_params['fontsize_label']
			
		if 'title' in self._int_params:
			plt.title(self._int_params['title'], fontsize=fontsize_label)
			
		if 'xlabel' in self._int_params:
			ax.set_xlabel(self._int_params['xlabel'], fontsize=fontsize_label)
				
		if 'ylabel' in self._int_params:
			ax.set_ylabel(self._int_params['ylabel'], fontsize=fontsize_label)
			
		if 'isgrid' in self._int_params:
			if self._int_params['isgrid'] :
				ax.grid()
			
		if 'xlim' in self._int_params:
			plt.xlim(self._int_params['xlim'][0], self._int_params['xlim'][1])
			
		if 'ylim' in self._int_params:
			plt.ylim(self._int_params['ylim'][0], self._int_params['ylim'][1])
			
		if 'margin_top' in self._int_params:
			plt.subplots_adjust(top=self._int_params['margin_top'])
		if 'margin_bottom' in self._int_params:
			plt.subplots_adjust(bottom=self._int_params['margin_bottom'])
		if 'margin_right' in self._int_params:
			plt.subplots_adjust(right=self._int_params['margin_right'])
		if 'margin_left' in self._int_params:
			plt.subplots_adjust(left=self._int_params['margin_left'])
			
		if 'xticks' in self._int_params:
			plt.yticks(self._int_params['xticks'])
		if 'yticks' in self._int_params:
			plt.yticks(self._int_params['yticks'])
			
		plt.gca().xaxis.set_tick_params(which='both', direction='in', bottom=True, top=True, left=True, right=True)
		plt.gca().yaxis.set_tick_params(which='both', direction='in', bottom=True, top=True, left=True, right=True)
		
		
		filepath = 'test.bmp'
		plt.savefig('test.jpg')
		Image.open('test.jpg').save(filepath, 'BMP')
		
if __name__ == '__main__':
	from datetime import datetime
	time_record = []
	
	
	data_Xp = []
	data_Yp = []
	for i in range(0,80):
		data_Xp.append(i)
		data_Yp.append(25*(i % 10))
		
	for i in range(0,10):
		controller = CMatplotLibController()
		controller.InitCommonParams()
		
		start = datetime.now()
		
		controller.ExportGraph(data_Xp, data_Yp)
		
		elapsed_time = (datetime.now() - start) 
		
		time_record.append(elapsed_time.microseconds)
		
		
	print('- Time Records -')
	print(time_record)
	
	from statistics import mean
	
	print('- Time Stats -')
	print('Count: {0:d} '.format(len(time_record)))
	print('Avr: {0:.1f} msec'.format(mean(time_record) / 1000))
	print('Min: {0:.1f} msec'.format(min(time_record) / 1000))
	print('Max: {0:.1f} msec'.format(max(time_record) / 1000))
	plt.show()
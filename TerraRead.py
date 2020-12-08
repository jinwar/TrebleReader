import numpy as np
import matplotlib.pyplot as plt
from glob import glob
import h5py
from datetime import datetime

class TerraRead_V1:
    
    def __init__(self,filename):
        self.filename = filename
        self.fp = h5py.File(filename,'r')
        
    def get_frame_list(self):
        self.framelist = list(self.fp['deformation'].keys())
        
    def get_data_shape(self):
        Nt = 0
        for i,f in enumerate(self.framelist):
            Nt += self.fp['deformation'][f].shape[0]
        Nx = self.fp['deformation'][self.framelist[0]].shape[1]
        return Nt,Nx
    
    def read_data(self):
        # get frame list
        framelist = list(self.fp['deformation'].keys())
        # get data size
        Nt = 0
        for i,f in enumerate(framelist):
            Nt += self.fp['deformation'][f].shape[0]
        Nx = self.fp['deformation'][framelist[0]].shape[1]
        # read data
        data = np.zeros((Nt,Nx))
        i = 0
        for f in framelist:
            n = self.fp['deformation'][f].shape[0]
            data[i:i+n,:] = self.fp['deformation'][f][:,:]
            i += n
        self.data = data
        self.dt = self.fp['/'].attrs['dT_dec']
        self.dx = self.fp['/'].attrs['dx_dec']
        self.start_time = datetime.fromtimestamp(
            self.fp['gps_pps/'+list(self.fp['gps_pps'].keys())[0]].attrs['acq_time'])
       
    def apply_gauge_length(self,gauge_length_N):
        n = gauge_length_N//2
        data = self.data
        strain_data = np.zeros_like(data)
        for i in range(n,data.shape[1]-n):
            strain_data[:,i] = data[:,i+n]-data[:,i-n]
        
        self.strain_data = strain_data
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
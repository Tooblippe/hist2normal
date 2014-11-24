# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 18:41:13 2014
@author: tobie

Simple function to draw a histogram and normal distribution plot

"""

import scipy.stats as stats
import matplotlib.pyplot as plt
from matplotlib import *


def histplot( means, htitle='title', hxlabel='xlabel', hylabel='ylabel', bins =15, fz=15, filename=None):
    """
        Create a histogram and normal distribution plot of means
    """
    mu, sigma = stats.norm.fit(means)
    n, bins, patches = plt.hist(means, bins, normed=0, facecolor='green', alpha=0.75)
    y = mlab.normpdf( bins, mu, sigma)
    l = plt.plot(bins, y/max(y)*max(n), 'r--', linewidth=2)
    
    title(htitle + r' ($\mu$ =' + str(round(mu,1)) +', $\sigma$ =' + str(round(sigma,2)) +')', fontsize=fz)
    xlabel(hxlabel, fontsize=fz)
    ylabel(hylabel, fontsize=fz)
    # TODO: also generalise figsize
    figsize( 10, 5 )  
    # TODO :  be able to set this
    #
    #plt.xlim(min(means),max(means))
    # TODO: plot a vertical line at the mean and st deviation. plot( (x,x,), (y,y)) 
    # TODO: add label to the plot
    if filename:    
     savefig(filename+'.png', bbox_inches='tight')
    return mu, sigma, bins, y, l, n, patches
    
    
def test_hist_plot():
    """
        Creates an example plot
    """
    histplot( rand.normal( 50, 1, 1000), htitle='Sample Plot', hxlabel='x', hylabel='test', filename='test')
    



    
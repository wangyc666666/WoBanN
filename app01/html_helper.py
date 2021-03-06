#coding:utf-8
import urllib.request
import json
import sys
from django.utils.safestring import mark_safe


class PageInfo:
	
	def __init__ (self,current_page,all_count,per_item=1):
		self.CurrentPage = current_page
		self.AllCount = all_count
		self.PerItem = per_item
	
	@property
	def start(self):
		return (self.CurrentPage-1)*self.PerItem
	@property	
	def end(self):
		return self.CurrentPage*self.PerItem
	@property
	def all_page_count(self):
	
		temp=divmod(self.AllCount,self.PerItem)
		if temp[1]==0:
			all_page_count=temp[0]
		else:
			all_page_count=temp[0]+1
		return all_page_count
		
		
def Pager(page, all_page_count, url):
	page_html=[]

	first_html="<li> <a href = '%s'>首</a></li>" %(url)
	page_html.append(first_html)

	#if page <= 1:
	#	prev_html="<li><a href='#' >上一页</a></li>"
	#	page_html.append(prev_html)
	#else:
	#	prev_html="<li><span></span></li><li><a href='%s%d'>上一页</a></li>" %(url, page-1)
	#	page_html.append(prev_html)
        
	begin = page - 2
	end = page + 2
    
    
	#11个页码
	if all_page_count<6:
		begin = 0
		end  = all_page_count
    #大于11
	else:
		if page<6:
			begin = 0 
			end = 6
		else:
			if page + 6>all_page_count:
				begin = page - 2
				end = all_page_count
			else:
				begin = page - 3
				end = page + 2
            
        
    #for i in range(all_page_count):
	for i in range(begin,end):
        #当前页变色
		if page == i+1:
			a_html="<li><a class='on' href='%s%d'> %d </a></li>" %(url,i+1,i+1)
			page_html.append(a_html)
            
		else:
			a_html="<li><a href='%s%d'>%d</a></li>" %(url,i+1,i+1)
			page_html.append(a_html)
        
        
	#if page >= all_page_count :
	#	aft_html="<li></span></li><li><a href='#' >下一页</a></li>"
	#	page_html.append(aft_html)
	#else:
	#	aft_html="<li><span ></span></li><li><a href='%s%d'>下一页</a></li>" %(url, page+1)
	#	page_html.append(aft_html)
                     
        
	end_html="<li><span></span></li><li><a href='%s%d'>末</a></li></ul></div></div>"  %(url, all_page_count)
    
	page_html.append(end_html)
   
    
	page_string=mark_safe(''.join(page_html))
	return page_string
    



def get_client_ip(request):
    try:
        real_ip = request.META['HTTP_X_FORWARDED_FOR']
        regip = real_ip.split(",")[0]
    except:
        try:
            regip = request.META['REMOTE_ADDR']
        except:
            regip = ""
    return regip

def get_ip_area(request):
    regip=get_client_ip(request)
    try:
        apiurl = "http://ip.taobao.com/service/getIpInfo.php?ip=%s" %regip
        content = urllib.request.urlopen(apiurl).read()
        content=content.decode('utf-8')
        content=str(content)
        data = json.loads(content)['data']
        code = json.loads(content)['code']
        if code == 0:  
            return data

        else:
            return data
    except Exception as ex:
        return ex



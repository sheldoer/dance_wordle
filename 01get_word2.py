from xml.dom import minidom
import os

def main():
    #danmu=[]

    with open('E:/allcode/python_note/210207ciyun/danmu.xml','r',encoding='utf8') as fh:
        dom=minidom.parse(fh)
        # 获取根节点
        root=dom.documentElement
        # 获取某个元素节点的文本内容，先获取子文本节点，然后通过“data”属性获取文本内容


        with open('bullet.txt','w',encoding='gb18030') as fp:
            try:
                for i in range(1000):
                    name=root.getElementsByTagName('d')[i]
                    name_text_node=name.childNodes[0]
                    danmu=name_text_node.data
                    type(danmu)
                
                    fp.write(danmu)
                    fp.write('\n')
                #print(name_text_node.data)
            except:
                print('over!')
        #danmus=[str(i)+'\n' for i in danmu]

'''
    
if __name__ == '__main__':
    main()

import xdrlib,sys
import xlrd
import sys
import os

## Open excel
def open_excel(file):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception:
        print (str(e))
        
#根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的索引  ，by_name：Sheet1名称
def excel_table_byname(file, colnameindex=0, by_name=u'Sheet1'):
    data = open_excel(file) #打开excel文件
    table = data.sheet_by_name(by_name) #根据sheet名字来获取excel中的sheet
    nrows = table.nrows #行数  
    colnames = table.row_values(colnameindex) #某一行数据 
    list =[] #装读取结果的序列
    for rownum in range(0, nrows): #遍历每一行的内容
        row = table.row_values(rownum) #根据行号获取行
        if row: #如果行存在
            app = [] #一行的内容
            for i in range(len(colnames)): #一列列地读取行的内容
                if(isinstance(row[i],float)):
                    app.append(str(int(row[i])))
                else:
                    app.append(row[i])
            list.append(app) #装载数据
    return list

def gen_testcase(list):
    for i in range(0,len(list)):
        if(i>0):
            if os.path.exists(list[i][0]):
                test_dir = list[i][0]
                print ("folder is existing")
            else:
                os.mkdir(list[i][0])
                test_dir = list[i][0]
            cfg =  test_dir +'\\test_cfg.txt'
            txt =  open (cfg,'w')
            for j in range(1,len(list[i])):
                txt.write('{0} = {1} \n'.format(list[0][j],list[i][j]))
            txt.close()
            tcl = test_dir +'\\sim.tcl'
            sim_tcl = open(tcl,'w')
            sim_tcl.write('''set runtime 600ns
quit -sim
set current_dir [pwd]

set cfg_f [open $current_dir/$1/test_cfg.txt r]
scan "[read $cfg_f]" "%s" tc_name

#rm -rf ./$1/testcase.log
echo "current testcase dir:$current_dir"
#close $cfg_f
vsim +cfg_file=$current_dir/$1/test_cfg.txt -coverage -i -voptargs=+acc -vopt -uvmcontrol=all -msgmode both -sv_lib $current_dir/../../../3_lib/external -sv_lib $tool_path/uvm-1.1d/win64/uvm_dpi work.top +UVM_OBJECTION_TRACE +UVM_TESTNAME=$tc_name -l ./$1/testcase.log
close $cfg_f

#vsim +cfg_file=$current_dir/$1/test_cfg.txt -coverage -assertdebug -i -voptargs=+acc -vopt -uvmcontrol=all -msgmode both -sv_lib $current_dir/../../../3_lib/external -sv_lib $tool_path/uvm-1.1d/win64/uvm_dpi work.top work.dma_assertion_ip work.dma_binding_module +UVM_OBJECTION_TRACE +UVM_TESTNAME=c_simple_test_dn -l testcase.log
#add wave -h -position insertpoint sim:/top/m_vif_apb/*
#add wave -h -position insertpoint sim:/top/m_vif_sif0/*
add wave -h -position insertpoint sim:/top/m_vif_axi/*
#add wave -position insertpoint sim:/top/dut/dma_write/*
add wave -position insertpoint sim:/top/dut/wready
add wave -position insertpoint sim:/top/dut/wflow_en
add wave -position insertpoint sim:/top/dut/unalign
add wave -position insertpoint sim:/top/dut/wlast
add wave -position insertpoint sim:/top/dut/split_final
add wave -position insertpoint sim:/top/dut/bvalid
#run $runtime
run -all
wave zoomfull
''')
            sim_tcl.close()

def main():
   tables = excel_table_byname(sys.argv[1])
   gen_testcase(tables)
   print (tables[0][0])

if __name__=="__main__":
    main()
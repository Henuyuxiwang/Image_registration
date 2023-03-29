%% 图像批量对齐图片
%%可正常运行
%%采用最大稳定极值区域（MSER)特征
%%采用前后帧图像匹配循环修正图像，对齐。
% This code is used to register images，
% 图像批量对齐图片，采用最大稳定极值区域（MSER)特征，采用前后帧图像匹配循环修正图像，对齐
% Author: yuxi
% Date: 2023-03-29

close all;
clear all;
clc

selpath = uigetdir('*.*','选择预处理文件夹')
path_origin=selpath;
%path_new= uigetdir('*.*','选择处理后的文件夹');     % 新路径，需提前创建
img_path_list=dir(strcat(path_origin,'*/*.tiff'));   %提取.jpg图片
img_num=length(img_path_list);        % 统计
h=waitbar(0,'please wait');

for j=2:img_num
    img_name_old=img_path_list(j).name;               % 原图片名
    FIXED_name=img_path_list(j-1).name;
    image=imread(strcat(path_origin,'/',img_name_old));   % 读取
    FIXED=imread(strcat(path_origin,'/',FIXED_name));
    [MOVINGREG] = registerImages2(image,FIXED);
    imwrite(MOVINGREG.RegisteredImage,strcat(path_origin,'/',img_name_old));     % 重命名
    str=['运行中...',num2str(j/img_num*100),'%'];
    waitbar(j/1000,h,str)
end
delete(h);
 disp(['已完成']);

                
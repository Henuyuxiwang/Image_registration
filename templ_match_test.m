% This function is used to test template matching
% It reads two images, crops a template from the first image, and then matches the template to the second image
% It then displays the matched image and the cropped template
% 此函数用于测试模板匹配
% 它读取两个图像，从第一个图像中裁剪出一个模板，然后将模板与第二个图像匹配
% 然后显示匹配的图像和裁剪的模板
function templ_match_test()
    %读参考图像
    img0=imread("D:/Image_registration/image_date/10450-10450-10450.tiff");
    %img1=imread("D:/Image_registration/image_date/10724-10724-10724.tiff");
    img1=imread("D:/Image_registration/image_date/10750-10750-10750.tiff");
    %imwrite("D:/Image_registration/image_date/0.tiff", img0);
    %se = translate(strel(1), [50 140]);%将一个平面结构化元素分别向下和向右移动30个位置
    %img1 = imdilate(img1,se);%利用膨胀函数平移图像
    imshow(img0);

    rect = getrect;
    % 获取框选区域
    template = imcrop(img0, rect);
    % 显示模板
    imshow(template);
    
    result = normxcorr2(template, img1);
    %根据图像的大小，计算空间域或频域中的互相关性。
    % 通过预先计算运行总和来计算局部总和。
    % 使用局部总和来归一化互相关性以获得相关系数。
    
    % 获取匹配结果
    [max_val, max_idx] = max(result(:));
    [max_row, max_col] = ind2sub(size(result), max_idx);
    
    % 获取配准后的图像
    top_left = [max_col - size(template, 2), max_row - size(template, 1)];
    bottom_right = [max_col, max_row];
    img_registered = insertShape(img1, 'Rectangle', [top_left, bottom_right - top_left], 'LineWidth', 2, 'Color', 'red');
    
    % 显示配准后的图像
    figure(1)
    imshow(img_registered);
    img_registered1 = img1(top_left(2):bottom_right(2), top_left(1):bottom_right(1), :);
    % 裁剪配准后的图像
    figure(2)
    imshow(img_registered1);
 
end
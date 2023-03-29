function [MOVINGREG] = registerImages2_1(MOVING,FIXED)
%registerImages  使用Registration Estimator应用程序自动生成的代码注册灰度图像。
%  [MOVINGREG] = registerImages(MOVING,FIXED) 使用Registration Estimator应用程序自动生成的代码注册灰度图像
%  MOVING和FIXED。在应用程序中交互设置所有注册参数的值，并将结果存储在结构数组MOVINGREG中。

% 由registrationEstimator应用程序于2023年3月28日自动生成


% 基于特征的技术需要计算机视觉工具箱的许可证
checkLicense()

% 默认空间参考对象
fixedRefObj = imref2d(size(FIXED));
movingRefObj = imref2d(size(MOVING));

% 检测MSER特征
fixedPoints = detectMSERFeatures(FIXED,'ThresholdDelta',1.220000,'RegionAreaRange',[13 26163],'MaxAreaVariation',0.881875);
movingPoints = detectMSERFeatures(MOVING,'ThresholdDelta',1.220000,'RegionAreaRange',[13 26163],'MaxAreaVariation',0.881875);

% 提取特征
[fixedFeatures,fixedValidPoints] = extractFeatures(FIXED,fixedPoints,'Upright',true);
[movingFeatures,movingValidPoints] = extractFeatures(MOVING,movingPoints,'Upright',true);

% 匹配特征
indexPairs = matchFeatures(fixedFeatures,movingFeatures,'MatchThreshold',32.500000,'MaxRatio',0.325000);
fixedMatchedPoints = fixedValidPoints(indexPairs(:,1));
movingMatchedPoints = movingValidPoints(indexPairs(:,2));
MOVINGREG.FixedMatchedFeatures = fixedMatchedPoints;
MOVINGREG.MovingMatchedFeatures = movingMatchedPoints;

% 应用变换-由于算法的随机性质，运行结果可能不完全相同
tform = estimateGeometricTransform2D(movingMatchedPoints,fixedMatchedPoints,'affine');
MOVINGREG.Transformation = tform;
MOVINGREG.RegisteredImage = imwarp(MOVING, movingRefObj, tform, 'OutputView', fixedRefObj, 'SmoothEdges', true);

% 存储空间参考对象
MOVINGREG.SpatialRefObj = fixedRefObj;

end

function checkLicense()

% 检查计算机视觉工具箱的许可证
CVTStatus = license('test','Video_and_Image_Blockset');
if ~CVTStatus
    error(message('images:imageRegistration:CVTRequired'));
end

end

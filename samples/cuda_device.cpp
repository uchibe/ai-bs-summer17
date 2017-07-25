#include <iostream>
#include <opencv2/opencv.hpp>
#include <opencv2/core/cuda.hpp>

using namespace std;

int main() {
  cv::cuda::DeviceInfo info(0);
  cout <<
    "[CUDA Device 0]" << endl <<
    "name: " << info.name() << endl <<
    "majorVersion: " << info.majorVersion() << endl <<
    "minorVersion: " << info.minorVersion() << endl <<
    "multiProcessorCount: " << info.multiProcessorCount() << endl <<
    "sharedMemPerBlock: " << info.sharedMemPerBlock() << endl <<
    "freeMemory: " << info.freeMemory() << endl <<
    "totalMemory: " << info.totalMemory() << endl <<
    "isCompatible: " << info.isCompatible() << endl <<
    "supports(FEATURE_SET_COMPUTE_10): " << info.supports(cv::cuda::FEATURE_SET_COMPUTE_10) << endl <<
    "supports(FEATURE_SET_COMPUTE_11): " << info.supports(cv::cuda::FEATURE_SET_COMPUTE_11) << endl <<
    "supports(FEATURE_SET_COMPUTE_12): " << info.supports(cv::cuda::FEATURE_SET_COMPUTE_12) << endl <<
    "supports(FEATURE_SET_COMPUTE_13): " << info.supports(cv::cuda::FEATURE_SET_COMPUTE_13) << endl <<
    "supports(FEATURE_SET_COMPUTE_20): " << info.supports(cv::cuda::FEATURE_SET_COMPUTE_20) << endl <<
    "supports(FEATURE_SET_COMPUTE_21): " << info.supports(cv::cuda::FEATURE_SET_COMPUTE_21) << endl <<
    "supports(FEATURE_SET_COMPUTE_30): " << info.supports(cv::cuda::FEATURE_SET_COMPUTE_30) << endl <<
    "supports(FEATURE_SET_COMPUTE_35): " << info.supports(cv::cuda::FEATURE_SET_COMPUTE_35) << endl;
  
  return 0;
}

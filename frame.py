# 
import dlib

print("Is CUDA enabled:", dlib.DLIB_USE_CUDA)  # Should print True
print("Number of GPUs:", dlib.cuda.get_num_devices())  # Should return > 0
from cudaTestProgram import * 

temporalTests = [
    CudaTestProgram("temporal/device_bad_alloc.cu",
        testCases=[ 
            CudaTestCase(CudaError.OOM),
        ]),
    CudaTestProgram("temporal/device_bad_memcpy.cu",
        macros={'CPY_SIZE':'17','DST_SIZE':'17','SRC_SIZE':'16'},
        testCases=[ 
            CudaTestCase(CudaError.GLB_W),
        ]),
    CudaTestProgram("temporal/device_bad_memcpy.cu",
        macros={'CPY_SIZE':'17','DST_SIZE':'16','SRC_SIZE':'17'},
        testCases=[ 
            CudaTestCase(CudaError.GLB_W),
        ]),
    CudaTestProgram("temporal/device_bad_memset.cu",
        testCases=[ 
            CudaTestCase(CudaError.GLB_W),
        ]),
    CudaTestProgram("temporal/device_uninit_memcpy.cu",
        macros={'CPY_SIZE':'16','DST_SIZE':'16','SRC_SIZE':'16'},
        testCases=[ 
            CudaTestCase(CudaError.GLB_W),
        ]),
    CudaTestProgram("temporal/device_early_dealloc_w.cu",
        testCases=[ 
            CudaTestCase(CudaError.GLB_W),
        ]),
    CudaTestProgram("temporal/device_uninit_r.cu",
        testCases=[ 
            CudaTestCase(CudaError.GLB_R),
        ]),
    CudaTestProgram("temporal/host_bad_alloc.cu",
        testCases=[ 
            CudaTestCase(CudaError.OOM),
        ]),
    CudaTestProgram("temporal/host_bad_memcpy.cu",
        macros={'CPY_SIZE':'17','DST_SIZE':'16','SRC_SIZE':'17'},
        testCases=[ 
            CudaTestCase(CudaError.ARG),
        ]),
    CudaTestProgram("temporal/host_bad_memcpy.cu",
        macros={'CPY_SIZE':'17','DST_SIZE':'17','SRC_SIZE':'16'},
        testCases=[ 
            CudaTestCase(CudaError.GLB_W),
        ]),
    CudaTestProgram("temporal/host_bad_memset.cu",
        testCases=[ 
            CudaTestCase(CudaError.ARG),
        ]),
    CudaTestProgram("temporal/host_uninit_memcpy.cu",
        macros={'CPY_SIZE':'16','DST_SIZE':'16','SRC_SIZE':'16'},
        testCases=[ 
            CudaTestCase(CudaError.GLB_W),
        ]),
    CudaTestProgram("temporal/host_early_dealloc_w.cu",
        testCases=[ 
            CudaTestCase(CudaError.GLB_W),
        ]),
    CudaTestProgram("temporal/host_uninit_r.cu",
        testCases=[ 
            CudaTestCase(CudaError.GLB_R),
        ]),
    CudaTestProgram("temporal/leaky_pointers.cu",
        macros={'LOCAL_LEAK_WITHIN_WARP':None,'TO_GLOBAL_PTR':None},
        testCases=[ 
            CudaTestCase(CudaError.LCL_R),
        ]),
    CudaTestProgram("temporal/leaky_pointers.cu",
        macros={'LOCAL_LEAK_WITHIN_WARP':None,'TO_SHARED_PTR':None},
        testCases=[ 
            CudaTestCase(CudaError.LCL_R),
        ]),
    CudaTestProgram("temporal/leaky_pointers.cu",
        macros={'SHARED_LEAK_ACROSS_BLOCKS':None,'TO_GLOBAL_PTR':None},
        testCases=[ 
            CudaTestCase(CudaError.SHR_R),
        ]),
    CudaTestProgram("temporal/leaky_pointers_child_kernel.cu",
        macros={'LEAK_LOCAL':None,'DIRECT':None},
        testCases=[ 
            CudaTestCase(CudaError.LCL_R),
        ]),
    CudaTestProgram("temporal/leaky_pointers_child_kernel.cu",
        macros={'LEAK_SHARED':None,'DIRECT':None},
        testCases=[ 
            CudaTestCase(CudaError.SHR_R),
        ]),
    CudaTestProgram("temporal/leaky_pointers_child_kernel.cu",
        macros={'LEAK_LOCAL':None,'INDIRECT':None},
        testCases=[ 
            CudaTestCase(CudaError.LCL_R),
        ]),
    CudaTestProgram("temporal/leaky_pointers_child_kernel.cu",
        macros={'LEAK_SHARED':None,'INDIRECT':None},
        testCases=[ 
            CudaTestCase(CudaError.SHR_R),
        ]),
    CudaTestProgram("temporal/local_uninit_r.cu",
        expectedCompilerWarnings=[CudaWarning.VAR_USED_BEFORE_SET],
        testCases=[ 
            CudaTestCase(CudaError.LCL_R),
        ]),
    CudaTestProgram("temporal/pitched_ptr_bad_memcpy.cu",
        macros={'HTD_ROW_OFFSET':'1','DTH_ROW_OFFSET':'0'},
        testCases=[ 
            CudaTestCase(CudaError.NO_ERR),
        ]),
    CudaTestProgram("temporal/pitched_ptr_bad_memcpy.cu",
        macros={'HTD_ROW_OFFSET':'-1','DTH_ROW_OFFSET':'0'},
        testCases=[ 
            CudaTestCase(CudaError.NO_ERR),
        ]),
    CudaTestProgram("temporal/pitched_ptr_bad_memcpy.cu",
        macros={'HTD_ROW_OFFSET':'16','DTH_ROW_OFFSET':'0'},
        testCases=[ 
            CudaTestCase(CudaError.PITCH_ARG),
        ]),
    CudaTestProgram("temporal/pitched_ptr_bad_memcpy.cu",
        macros={'HTD_ROW_OFFSET':'0','DTH_ROW_OFFSET':'1'},
        testCases=[ 
            CudaTestCase(CudaError.NO_ERR),
        ]),
    CudaTestProgram("temporal/pitched_ptr_bad_memcpy.cu",
        macros={'HTD_ROW_OFFSET':'0','DTH_ROW_OFFSET':'-1'},
        testCases=[ 
            CudaTestCase(CudaError.NO_ERR),
        ]),
    CudaTestProgram("temporal/pitched_ptr_bad_memcpy.cu",
        macros={'HTD_ROW_OFFSET':'0','DTH_ROW_OFFSET':'16'},
        testCases=[ 
            CudaTestCase(CudaError.PITCH_ARG),
        ]),
    CudaTestProgram("temporal/shared_extern_uninit_r.cu",
        testCases=[ 
            CudaTestCase(CudaError.SHR_R),
        ]),
    CudaTestProgram("temporal/shared_uninit_r.cu",
        expectedCompilerWarnings=[CudaWarning.VAR_USED_BEFORE_SET],
        testCases=[ 
            CudaTestCase(CudaError.SHR_R),
        ]),
]

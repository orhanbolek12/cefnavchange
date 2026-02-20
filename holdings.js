// CEF Holdings Data - Extracted from all_holdings.json
// Each CEF maps to an array of { symbol, weight } objects
// Weight = percentage of the portfolio

const CEF_HOLDINGS = {
    "BME": [
        {"symbol":"JNJ","weight":8.22},{"symbol":"LLY","weight":7.81},{"symbol":"ABT","weight":5.96},
        {"symbol":"ABBV","weight":4.74},{"symbol":"UNH","weight":4.2},{"symbol":"BSX","weight":4.05},
        {"symbol":"TMO","weight":3.5},{"symbol":"SYK","weight":3.47},{"symbol":"MDT","weight":3.44},
        {"symbol":"AMGN","weight":3.24},{"symbol":"EW","weight":3.07},{"symbol":"ALNY","weight":2.73},
        {"symbol":"ISRG","weight":2.62},{"symbol":"GILD","weight":1.92},{"symbol":"MCK","weight":1.75},
        {"symbol":"DHR","weight":1.69},{"symbol":"COR","weight":1.6},{"symbol":"INSM","weight":1.45},
        {"symbol":"MRK","weight":1.43},{"symbol":"BDX","weight":1.39},{"symbol":"LH","weight":1.13},
        {"symbol":"RYTM","weight":1.07},{"symbol":"HCA","weight":1.03},{"symbol":"VRTX","weight":0.97},
        {"symbol":"REGN","weight":0.96},{"symbol":"AZN","weight":0.96},{"symbol":"TEVA","weight":0.94},
        {"symbol":"A","weight":0.91},{"symbol":"DGX","weight":0.89},{"symbol":"IDXX","weight":0.85},
        {"symbol":"BMY","weight":0.85},{"symbol":"ARGX","weight":0.82},{"symbol":"BIIB","weight":0.79},
        {"symbol":"WAT","weight":0.6},{"symbol":"IQV","weight":0.59},{"symbol":"INCY","weight":0.54},
        {"symbol":"PFE","weight":0.52},{"symbol":"EXAS","weight":0.52},{"symbol":"CI","weight":0.52},
        {"symbol":"WST","weight":0.51},{"symbol":"VEEV","weight":0.51},{"symbol":"DXCM","weight":0.49},
        {"symbol":"ELV","weight":0.49},{"symbol":"PODD","weight":0.47},{"symbol":"CVS","weight":0.47},
        {"symbol":"GH","weight":0.38},{"symbol":"NTRA","weight":0.37},{"symbol":"THC","weight":0.37},
        {"symbol":"COO","weight":0.36},{"symbol":"CNC","weight":0.34},{"symbol":"RGEN","weight":0.33},
        {"symbol":"BMRN","weight":0.32}
    ],
    "BMEZ": [
        {"symbol":"ALNY","weight":5.36},{"symbol":"VEEV","weight":3.46},{"symbol":"INSM","weight":2.59},
        {"symbol":"ABT","weight":2.46},{"symbol":"WST","weight":2.46},{"symbol":"PODD","weight":1.81},
        {"symbol":"EW","weight":1.68},{"symbol":"JNJ","weight":1.6},{"symbol":"RGEN","weight":1.59},
        {"symbol":"MDT","weight":1.57},{"symbol":"GMAB","weight":1.54},{"symbol":"EXAS","weight":1.44},
        {"symbol":"THC","weight":1.43},{"symbol":"TEVA","weight":0.9},{"symbol":"WAT","weight":0.76},
        {"symbol":"INCY","weight":0.74},{"symbol":"BSX","weight":0.67},{"symbol":"SYK","weight":1.08},
        {"symbol":"MCK","weight":1.01}
    ],
    "GRX": [
        {"symbol":"ABBV","weight":4.35},{"symbol":"THC","weight":3.46},{"symbol":"JNJ","weight":2.94},
        {"symbol":"CI","weight":2.85},{"symbol":"OPCH","weight":2.82},{"symbol":"TEVA","weight":2.54},
        {"symbol":"COR","weight":2.51},{"symbol":"MRK","weight":2.46},{"symbol":"HALO","weight":2.42},
        {"symbol":"POST","weight":2.38},{"symbol":"LH","weight":2.22},{"symbol":"KR","weight":2.13},
        {"symbol":"ZBH","weight":2.1},{"symbol":"BRBR","weight":2.07},{"symbol":"SJM","weight":2.06},
        {"symbol":"ELV","weight":2.05},{"symbol":"NSRGY","weight":2.03},{"symbol":"CVS","weight":1.97},
        {"symbol":"COO","weight":1.87},{"symbol":"ITGR","weight":1.86},{"symbol":"CHE","weight":1.81},
        {"symbol":"AMGN","weight":1.79},{"symbol":"CPB","weight":1.7},{"symbol":"SYK","weight":1.69},
        {"symbol":"HSIC","weight":1.68},{"symbol":"MCK","weight":1.58},{"symbol":"AZN","weight":1.57},
        {"symbol":"ABT","weight":1.56},{"symbol":"BMY","weight":1.38},{"symbol":"UL","weight":1.31},
        {"symbol":"VRTX","weight":1.29},{"symbol":"MDT","weight":1.21},{"symbol":"TMO","weight":1.09},
        {"symbol":"WAT","weight":0.96},{"symbol":"HCA","weight":0.94},{"symbol":"BDX","weight":0.93},
        {"symbol":"IQV","weight":0.84},{"symbol":"RDY","weight":0.83},{"symbol":"SNY","weight":0.75},
        {"symbol":"DGX","weight":0.7},{"symbol":"NBIX","weight":0.67},{"symbol":"LLY","weight":0.66},
        {"symbol":"EW","weight":0.64},{"symbol":"REGN","weight":0.62}
    ],
    "HQH": [
        {"symbol":"QURE","weight":7.65},{"symbol":"AMGN","weight":3.05},{"symbol":"VRTX","weight":2.52},
        {"symbol":"ARGX","weight":2.46},{"symbol":"ALNY","weight":2.3},{"symbol":"CYTK","weight":2.16},
        {"symbol":"REGN","weight":2.15},{"symbol":"BMRN","weight":2.15},{"symbol":"LLY","weight":2.06},
        {"symbol":"ABT","weight":1.88},{"symbol":"INSM","weight":1.76},{"symbol":"RARE","weight":1.72},
        {"symbol":"PCVX","weight":1.62},{"symbol":"GILD","weight":1.56},{"symbol":"SRPT","weight":1.46},
        {"symbol":"TVTX","weight":1.46},{"symbol":"AKRO","weight":1.41},{"symbol":"BNTX","weight":1.41},
        {"symbol":"XENE","weight":1.35},{"symbol":"MDT","weight":1.23},{"symbol":"DHR","weight":1.1},
        {"symbol":"ISRG","weight":1.09},{"symbol":"INSP","weight":1.06},{"symbol":"BDX","weight":1.0},
        {"symbol":"ABBV","weight":0.98},{"symbol":"ARWR","weight":0.97},{"symbol":"IMVT","weight":0.96},
        {"symbol":"DNLI","weight":0.85},{"symbol":"ZTS","weight":0.86},{"symbol":"CVS","weight":0.82},
        {"symbol":"AZN","weight":0.8},{"symbol":"NBIX","weight":0.8},{"symbol":"CRNX","weight":0.79},
        {"symbol":"BSX","weight":0.73},{"symbol":"ELV","weight":0.7},{"symbol":"EYPT","weight":0.68},
        {"symbol":"MOH","weight":0.66},{"symbol":"RNA","weight":0.63},{"symbol":"AXSM","weight":0.62}
    ],
    "HQL": [
        {"symbol":"QURE","weight":7.49},{"symbol":"VRTX","weight":3.34},{"symbol":"AMGN","weight":3.0},
        {"symbol":"ALNY","weight":2.99},{"symbol":"INSM","weight":2.83},{"symbol":"ARGX","weight":2.72},
        {"symbol":"REGN","weight":2.62},{"symbol":"BMRN","weight":2.38},{"symbol":"CYTK","weight":2.12},
        {"symbol":"RARE","weight":2.05},{"symbol":"XENE","weight":1.66},{"symbol":"AKRO","weight":1.65},
        {"symbol":"PCVX","weight":1.62},{"symbol":"BNTX","weight":1.51},{"symbol":"ARWR","weight":1.43},
        {"symbol":"TVTX","weight":1.41},{"symbol":"PSNL","weight":1.36},{"symbol":"DNLI","weight":1.35},
        {"symbol":"RNA","weight":1.24},{"symbol":"SRPT","weight":1.2},{"symbol":"IDYA","weight":1.13},
        {"symbol":"CRNX","weight":1.07},{"symbol":"IMVT","weight":1.04},{"symbol":"GILD","weight":1.03},
        {"symbol":"AXSM","weight":0.93},{"symbol":"MREO","weight":0.83},{"symbol":"EWTX","weight":0.83},
        {"symbol":"ABVX","weight":0.81},{"symbol":"ASND","weight":0.78},{"symbol":"EYPT","weight":0.77},
        {"symbol":"NBIX","weight":0.74},{"symbol":"NAMS","weight":0.7},{"symbol":"IONS","weight":0.56},
        {"symbol":"TEM","weight":0.95},{"symbol":"MEN","weight":0.95}
    ],
    "THW": [
        {"symbol":"ABVX","weight":8.86},{"symbol":"QURE","weight":8.5},{"symbol":"AZN","weight":5.41},
        {"symbol":"ABBV","weight":3.99},{"symbol":"ABT","weight":3.83},{"symbol":"LLY","weight":3.6},
        {"symbol":"SNY","weight":3.51},{"symbol":"RHHBY","weight":3.34},{"symbol":"TEVA","weight":3.21},
        {"symbol":"MDT","weight":2.94},{"symbol":"ISRG","weight":2.46},{"symbol":"MRK","weight":2.41},
        {"symbol":"DHR","weight":2.22},{"symbol":"NVO","weight":2.01},{"symbol":"CVS","weight":1.77},
        {"symbol":"BDX","weight":1.74},{"symbol":"ZTS","weight":1.72},{"symbol":"BSX","weight":1.67},
        {"symbol":"TMO","weight":1.67},{"symbol":"ARGX","weight":1.64},{"symbol":"NAMS","weight":1.53},
        {"symbol":"VTR","weight":1.53},{"symbol":"UNH","weight":1.45},{"symbol":"MREO","weight":1.39},
        {"symbol":"EXAS","weight":1.36},{"symbol":"WELL","weight":1.33},{"symbol":"SYK","weight":1.27},
        {"symbol":"BAYRY","weight":1.13},{"symbol":"HUM","weight":1.12},{"symbol":"BMY","weight":1.11},
        {"symbol":"BNTX","weight":1.11},{"symbol":"INSP","weight":1.07},{"symbol":"PEAK","weight":1.05},
        {"symbol":"PFE","weight":1.02},{"symbol":"PRQR","weight":0.96},{"symbol":"CSL","weight":0.92},
        {"symbol":"ZBH","weight":0.91},{"symbol":"JNJ","weight":0.88},{"symbol":"ELV","weight":0.8},
        {"symbol":"MOH","weight":0.76},{"symbol":"PODD","weight":0.7},{"symbol":"DIS","weight":0.67},
        {"symbol":"ABBV","weight":0.61}
    ],
    "THQ": [
        {"symbol":"LLY","weight":9.5},{"symbol":"UNH","weight":9.5},{"symbol":"ABBV","weight":5.7},
        {"symbol":"JNJ","weight":5.2},{"symbol":"TMO","weight":4.5},{"symbol":"MRK","weight":4.1},
        {"symbol":"ABT","weight":3.9},{"symbol":"ISRG","weight":3.5},{"symbol":"ELV","weight":3.1},
        {"symbol":"DHR","weight":2.8},{"symbol":"PFE","weight":2.6},{"symbol":"MDT","weight":2.45},
        {"symbol":"BMY","weight":2.39},{"symbol":"INSP","weight":2.29},{"symbol":"BDX","weight":2.25},
        {"symbol":"SYK","weight":2.1},{"symbol":"BSX","weight":1.95},{"symbol":"VRTX","weight":1.85},
        {"symbol":"REGN","weight":1.7},{"symbol":"ZTS","weight":1.6},{"symbol":"WELL","weight":1.55},
        {"symbol":"VTR","weight":1.4},{"symbol":"HCA","weight":1.3},{"symbol":"CI","weight":1.25},
        {"symbol":"CVS","weight":1.15}
    ]
};

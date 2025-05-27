ELECTROMAGNETISM_DB = {
    "electrical_force": {
        "title": "Elektriksel Kuvvet",
        "content": "İki yük arasındaki etkileşim kuvveti",
        "equations": [
            "F = k\\frac{q_1q_2}{r^2}",
            "k = \\frac{1}{4\\pi\\epsilon_0} = 9 \\times 10^9 N\\cdot m^2/C^2"
        ]
    },
    
    "electric_field": {
        "title": "Elektriksel Alan",
        "content": "Birim yük başına düşen elektriksel kuvvet",
        "equations": [
            "\\vec{E} = \\frac{\\vec{F}}{q}",
            "\\vec{E} = k\\frac{Q}{r^2}\\hat{r}",
            "\\vec{E} = -\\nabla V"
        ]
    },
    
    "electric_potential": {
        "title": "Elektriksel Potansiyel",
        "content": "Birim yük başına düşen elektriksel potansiyel enerji",
        "equations": [
            "V = \\frac{U}{q}",
            "V = k\\frac{Q}{r}",
            "\\Delta V = -\\int \\vec{E} \\cdot d\\vec{l}"
        ]
    },
    
    "electric_potential_energy": {
        "title": "Elektriksel Potansiyel Enerji",
        "content": "Yükler arasındaki etkileşimden kaynaklanan enerji",
        "equations": [
            "U = k\\frac{q_1q_2}{r}",
            "U = qV",
            "U = \\frac{1}{2}CV^2"
        ]
    },
    
    "capacitance": {
        "title": "Sığa",
        "content": "Bir iletkenin yük depolama kapasitesi",
        "equations": [
            "C = \\frac{Q}{V}",
            "C = \\epsilon_0\\frac{A}{d}",
            "C_{seri} = \\frac{1}{\\sum\\frac{1}{C_i}}",
            "C_{paralel} = \\sum C_i"
        ]
    },
    
    "capacitor": {
        "title": "Kondansatör",
        "content": "Elektrik yükü ve enerji depolayan devre elemanı",
        "equations": [
            "Q = CV",
            "U = \\frac{1}{2}CV^2",
            "i = C\\frac{dV}{dt}"
        ]
    },
    
    "induction_current": {
        "title": "İndüksiyon Akımı",
        "content": "Değişen manyetik akıdan kaynaklanan elektrik akımı",
        "equations": [
            "\\mathcal{E} = -\\frac{d\\Phi_B}{dt}",
            "I = \\frac{\\mathcal{E}}{R}",
            "\\mathcal{E} = -L\\frac{dI}{dt}"
        ]
    },
    
    "magnetic_field": {
        "title": "Manyetik Alan",
        "content": "Hareketli yükler ve mıknatıslar tarafından oluşturulan alan",
        "equations": [
            "\\vec{F} = q\\vec{v} \\times \\vec{B}",
            "\\oint \\vec{B} \\cdot d\\vec{l} = \\mu_0I_{enc}",
            "B = \\frac{\\mu_0I}{2\\pi r}"
        ]
    },
    
    "charged_particle_motion": {
        "title": "Yüklü Parçacıkların Manyetik Alan İçerisindeki Hareketi",
        "content": "Manyetik alanda yüklü parçacıkların hareketi",
        "equations": [
            "F = qvB\\sin\\theta",
            "r = \\frac{mv}{qB}",
            "T = \\frac{2\\pi m}{qB}"
        ]
    },
    
    "self_induction": {
        "title": "Özindüksiyon",
        "content": "Bir devredeki akım değişiminin kendi üzerinde oluşturduğu indüksiyon",
        "equations": [
            "\\mathcal{E} = -L\\frac{dI}{dt}",
            "L = \\frac{N\\Phi_B}{I}",
            "U = \\frac{1}{2}LI^2"
        ]
    },
    
    "magnetic_flux": {
        "title": "Manyetik Akı",
        "content": "Manyetik alanın bir yüzeyden geçen toplam etkisi",
        "equations": [
            "\\Phi_B = \\int \\vec{B} \\cdot d\\vec{A}",
            "\\Phi_B = BA\\cos\\theta",
            "\\mathcal{E} = -\\frac{d\\Phi_B}{dt}"
        ]
    }
} 
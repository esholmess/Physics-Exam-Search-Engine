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
    },
    "ohm_kanunu": {
        "title": "Ohm Kanunu",
        "content": "Gerilim, akım ve direnç arasındaki ilişkiyi ifade eder.",
        "equations": [
            "V = I \\cdot R"
        ]
    },
    "guc_formulu": {
        "title": "Elektriksel Güç",
        "content": "Elektriksel güç, devrede harcanan enerjiyi ifade eder.",
        "equations": [
            "P = I \\cdot V",
            "P = I^2 \\cdot R"
        ]
    },
    "ohms_law": {
        "title": "Ohm Kanunu",
        "content": "Direnç, akım ve gerilim arasındaki ilişkiyi açıklar",
        "equations": [
            "V = IR"
        ]
    },
    "power_formula": {
        "title": "Elektriksel Güç",
        "content": "Güç, akım ve gerilim çarpımıyla hesaplanır",
        "equations": [
            "P = IV",
            "P = I^2R"
        ]
    },
    "wire_magnetic_field": {
        "title": "Telin Oluşturduğu Manyetik Alan",
        "content": "Düz bir telin çevresinde oluşan manyetik alan",
        "equations": [
            "B = k\\frac{2I}{d}"
        ]
    },
    "circle_magnetic_field": {
        "title": "Çemberin Merkezindeki Manyetik Alan",
        "content": "Dairesel telin merkezindeki manyetik alan",
        "equations": [
            "B = k\\frac{2\\pi I}{r}"
        ]
    },
    "solenoid_magnetic_field": {
        "title": "Selonoidde Manyetik Alan",
        "content": "Selonoid içinde oluşan manyetik alan",
        "equations": [
            "B = k\\frac{4\\pi NI}{l}"
        ]
    },
    "magnetic_force_wire": {
        "title": "Tele Etkiyen Manyetik Kuvvet",
        "content": "Manyetik alandaki bir tele etkiyen kuvvet",
        "equations": [
            "F = BIL",
            "F = BIL\\sin\\alpha"
        ]
    },
    "magnetic_force_particle": {
        "title": "Yüklü Cisme Etkiyen Manyetik Kuvvet",
        "content": "Manyetik alandaki yüklü parçacığa etkiyen kuvvet",
        "equations": [
            "F = Bqv"
        ]
    },
    "radius_magnetic_motion": {
        "title": "Manyetik Alanda Yörünge Yarıçapı",
        "content": "Yüklü parçacığın manyetik alanda izlediği dairesel yolun yarıçapı",
        "equations": [
            "r = \\frac{mv}{Bq}"
        ]
    },
    "emf_formula": {
        "title": "Elektromotor Kuvvet (EMK)",
        "content": "Hareketli bir iletkende oluşan emk",
        "equations": [
            "\\mathcal{E} = Blv",
            "\\mathcal{E} = Blv\\sin\\alpha"
        ]
    },
    "magnetic_flux_formula": {
        "title": "Manyetik Akı",
        "content": "Manyetik alanın bir yüzeyden geçiş ölçüsü",
        "equations": [
            "\\Phi = BA\\cos\\alpha"
        ]
    },
    "flux_change": {
        "title": "Manyetik Akı Değişimi",
        "content": "Akının ilk ve son değerleri arasındaki fark",
        "equations": [
            "\\Delta\\Phi = \\Phi_{son} - \\Phi_{ilk}"
        ]
    },
    "induced_emf": {
        "title": "İndüksiyon EMK",
        "content": "Manyetik akı değişiminden doğan elektromotor kuvvet",
        "equations": [
            "\\mathcal{E} = -\\frac{\\Delta\\Phi}{\\Delta t}"
        ]
    },
    "self_induced_emf": {
        "title": "Özindüksiyon EMK",
        "content": "Bir devredeki akım değişiminin oluşturduğu EMK",
        "equations": [
            "\\mathcal{E} = -L\\frac{\\Delta I}{\\Delta t}"
        ]
    },
    "max_emf": {
        "title": "Maksimum EMK",
        "content": "Manyetik akı değişimiyle oluşabilecek maksimum EMK",
        "equations": [
            "\\mathcal{E}_{max} = NBA\\omega"
        ]
    },
    "induced_current_conductor": {
        "title": "İletkendeki İndüksiyon Akımı",
        "content": "Zamana bağlı indüksiyon akımı",
        "equations": [
            "\\mathcal{E} = NBA\\omega\\sin(\\omega t)"
        ]
    },
    "transformer_voltage_turns": {
        "title": "Transformatörde Gerilim-Sarım İlişkisi",
        "content": "Gerilim oranı sarım sayısı oranına eşittir",
        "equations": [
            "\\frac{V_1}{V_2} = \\frac{N_1}{N_2}"
        ]
    },
    "transformer_power_relation": {
        "title": "Transformatörde Güç İlişkisi",
        "content": "Giriş ve çıkış güçleri eşit alınır (ideal transformatör)",
        "equations": [
            "V_1I_1 = V_2I_2"
        ]
    },
    "transformer_efficiency": {
        "title": "Transformatör Verimi",
        "content": "Transformatörün çıkış gücünün giriş gücüne oranı",
        "equations": [
            "\\eta = \\frac{V_2I_2}{V_1I_1}"
        ]
    }
}
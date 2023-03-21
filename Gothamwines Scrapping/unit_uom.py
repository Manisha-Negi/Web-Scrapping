import re


class uom_uom_pack:

    def get_unit_uom(Description):
        unit = ""
        uom = ""
        pack = ""
        Size = ""
        input = ""
        input2 = ""

        if re.search(
                "((\d+|\.\d+)+(|\s+)(L| L|L |lb| lb|Lb| Lb| LB| LB|Cup| Cup| Cup |sq yd| sq yd| sq yd |bottles| bottles |bottles | bottles|rolls| rolls|Count| Count|sq ft| sq ft|L | L|-L| fl oz | FOz| FOz|-FOz|Cubic Inches| Cubic Inches|-Cubic Inches|cubic in| cubic in|-cubic in|Gram| Gram |-Gram|Sq. Ft.|Ffl oz|FS| FS|-FS|fs| fs|-fs|Cubic Feet| Cubic Feet|-Cubic Feet|cubic feet| cubic feet|-cubic feet|Cubic Ft|Fluid Ounce| Fluid Ounce|-Fluid Ounce|fluid ounce| fluid ounce|-fluid ounce|Ct| Ct|-Ct|ct| ct|-ct|Dozen| Dozen|-Dozen|dozen| dozen|-dozen|inches|-inches|inches| ft.|-ft.|ft.| ft|-ft|ft|-mg| mg|mg|-Inch| mm|mm| fl.oz.| fl oz|FL OZ|Fl. Oz.|OZ|-Gal.|GAL|-LBS| LBS|LBS|-LB| LB|LB|lb|ML|-QTS| QTS|QTS|GAL|-GALLON| GALLON|GALLON|GRAMS|GRM|-GM.| GM|-GM |GM |-GR |GR | GR |-liter| liter|liter|-LTR| LTR|LTR|LT|CU.IN|QT|-QT| QT|CU. IN| Inch|INCH|IN|Cu.Ft|cuft|OUNCE|-ounce| ounce|-PINT| PINT|PINT|pound| pound|-pound|PT|QUART|SG|YD| Yard|-Yard|Yard|L | L |-L |Each | each|EACH |each |Gummies| Gummies |gummies | gummies|ea| ea |Ea| Ea|EA| EA| FZ|.Oz)(|\s+))|((\d+|\.\d+)+(|\s+)-(|\s+)(\d+|\.\d+)+(|\s+)(fl oz | FOz| FOz|-FOz|Cubic Inches| Cubic Inches|-Cubic Inches|cubic in| cubic in|-cubic in|Gram| Gram |-Gram|Sq. Ft.|Ffl oz|FS| FS|-FS|fs| fs|-fs|Cubic Feet| Cubic Feet|-Cubic Feet|cubic feet| cubic feet|-cubic feet|Fluid Ounce| Fluid Ounce|-Fluid Ounce|fluid ounce| fluid ounce|-fluid ounce|Ct| Ct|-Ct|ct| ct|-ct|Dozen| Dozen|-Dozen|dozen| dozen|-dozen|inches|-inches|inches| ft.|-ft.|ft.| ft|-ft|ft|-mg| mg|mg|-Inch| mm|mm| fl.oz.|Fl. Oz.| fl oz|FL OZ|OZ| GAL|-Gal.|-LBS| LBS|LBS|-LB| LB|LB|ML|-QTS| QTS|QTS|GAL|-GALLON| GALLON|GALLON|GRAMS|GRM|-GM.| GM|-GM |GM |-GR |GR | GR |-liter|liter|liter|-LTR| LTR|LTR|LT|CU.IN|QT|-QT| QT|CU. IN|INCH| Inch|IN|Cu.Ft|cu ft|OUNCE|-ounce| ounce|-PINT| PINT|PINT|pound| pound|-pound|PT|QUART|SG|YD| Yard|-Yard|Yard|L | L |-L |Each | each|EACH|ea| ea |Ea| Ea|EA| EA|L | L |-L| FZ|.Oz)(|\s+))|((\d+|\.\d+)+(|\s+)/(|\s+)(\d+|\.\d+)+(|\s+)(fl oz | FOz| FOz|-FOz|Cubic Inches| Cubic Inches|-Cubic Inches|cubic in| cubic in|-cubic in|Cubic Ft|Gram| Gram |-Gram|Sq. Ft.|Ffl oz|FS| FS|-FS|fs| fs|-fs|Cubic Feet| Cubic Feet|-Cubic Feet|cubic feet| cubic feet|-cubic feet|Fluid Ounce| Fluid Ounce|-Fluid Ounce|fluid ounce| fluid ounce|-fluid ounce|Ct| Ct|-Ct|ct| ct|-ct|Dozen| Dozen|-Dozen|dozen| dozen|-dozen|inches|-inches|inches| ft.|-ft.|ft.| ft|-ft|ft|-mg| mg|mg|-Inch| mm|mm| fl.oz.|Fl. Oz.| fl oz|FL OZ|OZ| GAL|-Gal.|-LBS| LBS|LBS|-LB| LB|LB|ML|-QTS| QTS|QTS|GAL|-GALLON| GALLON|GALLON|GRAMS|GRM|-GM.| GM|-GM |GM |-GR |GR | GR |-liter| liter|liter|-LTR| LTR|LTR|LT|CU.IN|QT|-QT| QT|CU. IN| Inch|INCH|IN|Cu.Ft|cu ft|OUNCE|-ounce| ounce|-PINT| PINT|PINT|pound| pound|-pound|PT|QUART|SG|YD| Yard|-Yard|Yard|L | L |-L |Each | each|EACH|ea| ea |Ea| Ea|EA| EA|Count| Count| FZ|.Oz)(|\s+))|((\d+|\.\d+)+(|\s+)x(|\s+)(\d+|\.\d+)+(|\s+)( FOz| FOz|-FOz|Cubic Inches| Cubic Inches|-Cubic Inches|cubic in| cubic in|-cubic in|Gram| Gram |-Gram|Sq. Ft.|Ffl oz|FS| FS|-FS|fs| fs|-fs|Cubic Feet| Cubic Feet|-Cubic Feet|cubic feet| cubic feet|-cubic feet|Fluid Ounce| Fluid Ounce|-Fluid Ounce|fluid ounce| fluid ounce|-fluid ounce|Ct| Ct|-Ct|ct| ct|-ct|Dozen| Dozen|-Dozen|dozen| dozen|-dozen|inches|-inches|inches| ft.|-ft.|ft.| ft|-ft|ft|-mg| mg|mg|-Inch| mm|mm| fl.oz.|Fl. Oz.| fl oz|FL OZ|OZ| GAL|-Gal.|-LBS| LBS|LBS|-LB| LB|LB|ML|-QTS| QTS|QTS|GAL|-GALLON| GALLON|GALLON|GRAMS|GRM|-GM.| GM|-GM |GM |-GR |GR | GR |-liter| liter|liter|-LTR| LTR|LTR|LT|CU.IN|QT|-QT| QT|CU. IN| Inch|INCH|IN|Cu.Ft|cu ft|OUNCE|-ounce| ounce|-PINT| PINT|PINT|pound| pound|-pound|PT|QUART|SG|YD| Yard|-Yard|Yard|L | L |-L |Each | each|EACH |each |Gummies| Gummies |gummies | gummies|Cubic Ft| FZ|.Oz)(|\s+))",
                Description, re.IGNORECASE):
            input = re.search(
                "((\d+|\.\d+)+(|\s+)(L| L|L |lb| lb|Lb| Lb| LB| LB|Cup| Cup| Cup |sq yd| sq yd| sq yd |bottles| bottles |bottles | bottles|rolls| rolls|Count| Count|L | L|-L|sq ft| sq ft|fl oz | FOz| FOz|-FOz|Cubic Inches| Cubic Inches|-Cubic Inches|cubic in| cubic in|-cubic in|Gram| Gram |-Gram|Sq. Ft.|Ffl oz|FS| FS|-FS|fs| fs|-fs|Cubic Feet| Cubic Feet|-Cubic Feet|cubic feet| cubic feet|-cubic feet|Fluid Ounce| Fluid Ounce|-Fluid Ounce|fluid ounce| fluid ounce|-fluid ounce|Ct| Ct|-Ct|ct| ct|-ct|Dozen| Dozen|-Dozen|dozen| dozen|-dozen|inches|-inches|inches| ft.|-ft.|ft.| ft|-ft|ft|-mg| mg|mg|-Inch| mm|mm| fl.oz.| fl oz|FL OZ|Fl. Oz.|OZ|-Gal.|GAL|-LBS| LBS|LBS|-LB| LB|LB|lb|ML|-QTS| QTS|QTS|GAL|-GALLON| GALLON|GALLON|GRAMS|GRM|-GM.| GM|-GM |GM |-GR |GR | GR |-liter| liter|liter|-LTR| LTR|LTR|LT|CU.IN|QT|-QT| QT|CU. IN| Inch|INCH|IN|Cu.Ft|cuft|OUNCE|-ounce| ounce|-PINT| PINT|PINT|pound| pound|-pound|PT|QUART|SG|YD| Yard|-Yard|Yard| Yard.|Yard.| Yard.|Yard.|L | L |-L |Each | each|EACH |each |Gummies| Gummies |gummies | gummies|Cubic Ft|Count| Count| EA| FZ|.Oz)(|\s+))|((\d+|\.\d+)+(|\s+)-(|\s+)(\d+|\.\d+)+(|\s+)(fl oz | FOz| FOz|-FOz|Cubic Inches| Cubic Inches|-Cubic Inches|cubic in| cubic in|-cubic in|Gram| Gram |-Gram|Sq. Ft.|Ffl oz|FS| FS|-FS|fs| fs|-fs|Cubic Feet| Cubic Feet|-Cubic Feet|cubic feet| cubic feet|-cubic feet|Fluid Ounce| Fluid Ounce|-Fluid Ounce|fluid ounce| fluid ounce|-fluid ounce|Ct| Ct|-Ct|ct| ct|-ct|Dozen| Dozen|-Dozen|dozen| dozen|-dozen|inches|-inches|inches| ft.|-ft.|ft.| ft|-ft|ft|-mg| mg|mg|-Inch| mm|mm| fl.oz.|Fl. Oz.| fl oz|FL OZ|OZ| GAL|-Gal.|-LBS| LBS|LBS|-LB| LB|LB|ML|-QTS| QTS|QTS|GAL|-GALLON| GALLON|GALLON|GRAMS|GRM|-GM.| GM|-GM |GM |-GR |GR | GR |-liter|liter|liter|-LTR| LTR|LTR|LT|CU.IN|QT|-QT| QT|CU. IN|INCH| Inch|IN|Cu.Ft|cu ft|OUNCE|-ounce| ounce|-PINT| PINT|PINT|pound| pound|-pound|PT|QUART|SG|YD| Yard|-Yard|Yard| Yard.|Yard.| Yard.|Yard.|L | L |-L |Each | each|EACH|ea| ea |Ea| Ea|EA| EA|Cubic Ft|Count| Count| FZ|.Oz)(|\s+))|((\d+|\.\d+)+(|\s+)-(\d+|\.\d+)+(|\s+)/(|\s+)(\d+|\.\d+)+(|\s+)(fl oz | FOz| FOz|-FOz|Cubic Inches| Cubic Inches|-Cubic Inches|cubic in| cubic in|-cubic in|Gram| Gram |-Gram|Sq. Ft.|Ffl oz|FS| FS|-FS|fs| fs|-fs|Cubic Feet| Cubic Feet|-Cubic Feet|cubic feet| cubic feet|-cubic feet|Fluid Ounce| Fluid Ounce|-Fluid Ounce|fluid ounce| fluid ounce|-fluid ounce|Ct| Ct|-Ct|ct| ct|-ct|Dozen| Dozen|-Dozen|dozen| dozen|-dozen|inches|-inches|inches| ft.|-ft.|ft.| ft|-ft|ft|-mg| mg|mg|-Inch| mm|mm| fl.oz.|Fl. Oz.| fl oz|FL OZ|OZ| GAL|-Gal.|-LBS| LBS|LBS|-LB| LB|LB|ML|-QTS| QTS|QTS|GAL|-GALLON| GALLON|GALLON|GRAMS|GRM|-GM.| GM|-GM |GM |-GR |GR | GR |-liter| liter|liter|-LTR| LTR|LTR|LT|CU.IN|QT|-QT| QT|CU. IN| Inch|INCH|IN|Cu.Ft|cu ft|OUNCE|-ounce| ounce|-PINT| PINT|PINT|pound| pound|-pound|PT|QUART|SG|YD| Yard|-Yard|Yard| Yard.|Yard.| Yard.|Yard.|L | L |-L |Each | each|EACH|ea| ea |Ea| Ea|EA| EA|Cubic Ft|Count| Count| FZ|.Oz)(|\s+))|((\d+|\.\d+)+(|\s+)-(\d+|\.\d+)+(|\s+)x(|\s+)(\d+|\.\d+)+(|\s+)( FOz| FOz|-FOz|Cubic Inches| Cubic Inches|-Cubic Inches|cubic in| cubic in|-cubic in|Gram| Gram |-Gram|Sq. Ft.|Ffl oz|FS| FS|-FS|fs| fs|-fs|Cubic Feet| Cubic Feet|-Cubic Feet|cubic feet| cubic feet|-cubic feet|Fluid Ounce| Fluid Ounce|-Fluid Ounce|fluid ounce| fluid ounce|-fluid ounce|Ct| Ct|-Ct|ct| ct|-ct|Dozen| Dozen|-Dozen|dozen| dozen|-dozen|inches|-inches|inches| ft.|-ft.|ft.| ft|-ft|ft|-mg| mg|mg|-Inch| mm|mm| fl.oz.|Fl. Oz.| fl oz|FL OZ|OZ| GAL|-Gal.|-LBS| LBS|LBS|-LB| LB|LB|ML|-QTS| QTS|QTS|GAL|-GALLON| GALLON|GALLON|GRAMS|GRM|-GM.| GM|-GM |GM |-GR |GR | GR |-liter| liter|liter|-LTR| LTR|LTR|LT|CU.IN|QT|-QT| QT|CU. IN| Inch|INCH|IN|Cu.Ft|cu ft|OUNCE|-ounce| ounce|-PINT| PINT|PINT|pound| pound|-pound|PT|QUART|SG|YD| Yard|-Yard|Yard| Yard.|Yard.| Yard.|Yard.|L | L |-L |Each | each|EACH |each |Gummies| Gummies |gummies | gummies|Cubic Ft|Count| Count| FZ|.Oz)(|\s+))",
                Description, re.IGNORECASE)
            if input:
                input = input.group()
            else:
                input = ""

            if (re.search(
                    "((\d+|\.\d+)+(|\s+)-(\d+|\.\d+)+(|\s+)/(|\s+)(\d+|\.\d+)+)|((|\s+)(\d+|\.\d+)+)|((\d+|\.\d+)+(|\s+)x(|\s+)(\d+|\.\d+)+)|((\d+|\.\d+)+)|((\d+|\.\d+)+(|\s+)/(|\s+)(\d+|\.\d+)+)",
                    input, re.IGNORECASE)):
                unit = re.search(
                    "((\d+|\.\d+)+(|\s+)-(\d+|\.\d+)+(|\s+)/(|\s+)(\d+|\.\d+)+)|((\d+|\.\d+)+(|\s+)-(|\s+)(\d+|\.\d+)+)|((\d+|\.\d+)+(|\s+)x(|\s+)(\d+|\.\d+)+)|((\d+|\.\d+)+)",
                    input, re.IGNORECASE)
                if unit:
                    unit = unit.group()
                else:
                    unit = ""

            if (re.search(
                    "((\d+|\.\d+)+(|\s+)-(|\s+)(\d+|\.\d+)+)|((\d+|\.\d+)+(|\s+)x(|\s+)(\d+|\.\d+)+)|((\d+|\.\d+)+)|((\d+|\.\d+)+(|\s+)/(|\s+)(\d+|\.\d+)+)",
                    Description, re.IGNORECASE)):
                uom = re.search(
                    "(L| L|L |lb| lb|Lb| Lb| LB| LB|Cup| Cup| Cup |sq yd| sq yd| sq yd |bottles| bottles |bottles | bottles|rolls| rolls|Count| Count|L | L|-L|sq ft| sq ft|fl oz | FOz| FOz|-FOz|Cubic Inches| Cubic Inches|-Cubic Inches|cubic in| cubic in|-cubic in|Gram| Gram |-Gram|Sq. Ft.|Ffl oz|FS| FS|-FS|fs| fs|-fs|Cubic Feet| Cubic Feet|-Cubic Feet|cubic feet| cubic feet|-cubic feet|Fluid Ounce| Fluid Ounce|-Fluid Ounce|fluid ounce| fluid ounce|-fluid ounce|Ct| Ct|-Ct|ct| ct|-ct|Dozen| Dozen|-Dozen|dozen| dozen|-dozen|inches|-inches|inches| ft.|-ft.|ft.| ft|-ft|ft|-mg| mg|mg|-Inch| mm|mm| fl.oz.| fl oz|FL OZ|Fl. Oz.|OZ|Count| Count|-Gal.|GAL|-LBS| LBS|LBS|-LB| LB|LB|ML|-QTS| QTS|QTS|GAL|-GALLON| GALLON|GALLON|GRAMS|GRM|-GM.| GM|-GM |GM |-GR |GR | GR |-liter| liter|liter|-LTR| LTR|LTR|LT|CU.IN|QT|-QT| QT|CU. IN|INCH|IN|Cu.Ft|cu ft|OUNCE|-ounce| ounce|-PINT| PINT|PINT|pound| pound|-pound|PT|QUART|SG|YD| Inch| Yard|-Yard|Yard|L | L |-L |Each | each|EACH |each |Gummies| Gummies |gummies | gummies|Cubic Ft|Count| Count| ea| FZ)",
                    input, re.IGNORECASE)
                if uom:
                    uom = uom.group()
                else:
                    uom = ""

        if uom == "":
            if (re.search(
                    "((\d+|\.\d+)+(|\s+)(L | L |-L |fl oz | cu.ft.| sq.ft.|cu.ft.|sq.ft.| EA |EA |markers| markers|-markers|marker| marker|-marker|Meter(s)|-Meter(s)|Meter| Meter|-Meter|-Volt| Volt|mcg|-mcg| mcg|kg|-kg| kg|-G |G | G | ea)(|\s+))|((\d+|\.\d+)+(|\s+)-(|\s+)(\d+|\.\d+)+(|\s+)(fl oz | cu.ft.| sq.ft.|cu.ft.|sq.ft.| EA |EA |markers| markers|-markers|marker| marker|-marker|Meter(s)|-Meter(s)|Meter| Meter|-Meter|-Volt| Volt|mcg|-mcg| mcg|kg|-kg| kg|-G |G | G | ea)(|\s+))|((\d+|\.\d+)+(|\s+)/(|\s+)(\d+|\.\d+)+(|\s+)( cu.ft.| sq.ft.|cu.ft.|sq.ft.| EA |EA |markers| markers|-markers|marker| marker|-marker|Meter(s)|-Meter(s)|Meter| Meter|-Meter|-Volt| Volt|mcg|-mcg| mcg|kg|-kg| kg|-G |G | G | ea)(|\s+))|((\d+|\.\d+)+(|\s+)x(|\s+)(\d+|\.\d+)+(|\s+)( cu.ft.| sq.ft.|cu.ft.|sq.ft.| EA |EA |markers| markers|-markers|marker| marker|-marker|Meter(s)|-Meter(s)|Meter| Meter|-Meter|-Volt| Volt|mcg|-mcg| mcg|kg|-kg| kg|-G |G | G |Each | each|EACH| ea)(|\s+))",
                    Description, re.IGNORECASE)):
                input = re.search(
                    "((\d+|\.\d+)+(|\s+)( fl oz | cu.ft.| sq.ft.|cu.ft.|sq.ft.| EA |EA |markers| markers|-markers|marker| marker|-marker|Meter(s)|-Meter(s)|Meter| Meter|-Meter|-Volt| Volt|mcg|-mcg| mcg|kg|-kg| kg|-G |G | G |Each | each|EACH |each |Gummies| Gummies |gummies | gummies)(|\s+))|((\d+|\.\d+)+(|\s+)-(|\s+)(\d+|\.\d+)+(|\s+)( cu.ft.| sq.ft.|cu.ft.|sq.ft.| EA |EA |markers| markers|-markers|marker| marker|-marker|Meter(s)|-Meter(s)|Meter| Meter|-Meter|-Volt| Volt|mcg|-mcg| mcg|kg|-kg| kg|-G |G | G |Each | each|EACH |each |Gummies| Gummies |gummies | gummies)(|\s+))|((\d+|\.\d+)+(|\s+)/(|\s+)(\d+|\.\d+)+(|\s+)( cu.ft.| sq.ft.|cu.ft.|sq.ft.| EA |EA |markers| markers|-markers|marker| marker|-marker|Meter(s)|-Meter(s)|Meter| Meter|-Meter|-Volt| Volt|mcg|-mcg| mcg|kg|-kg| kg|-G |G | G |Each | each|EACH |each |Gummies| Gummies |gummies | gummies)(|\s+))|((\d+|\.\d+)+(|\s+)x(|\s+)(\d+|\.\d+)+(|\s+)( cu.ft.| sq.ft.|cu.ft.|sq.ft.| EA |EA |markers| markers|-markers|marker| marker|-marker|Meter(s)|-Meter(s)|Meter| Meter|-Meter|-Volt| Volt|mcg|-mcg| mcg|kg|-kg| kg|-G |G | G |Each | each|EACH |each |Gummies| Gummies |gummies | gummies)(|\s+))",
                    Description, re.IGNORECASE)
                if input:
                    input = input.group()
                else:
                    input = ""

                if (re.search(
                        "((\d+|\.\d+)+(|\s+)-(\d+|\.\d+)+(|\s+)/(|\s+)(\d+|\.\d+)+)|((\d+|\.\d+)+(|\s+)-(|\s+)(\d+|\.\d+)+)|((\d+|\.\d+)+(|\s+)x(|\s+)(\d+|\.\d+)+)|((\d+|\.\d+)+)|((\d+|\.\d+)+(|\s+)/(|\s+)(\d+|\.\d+)+)",
                        input, re.IGNORECASE)):
                    unit = re.search(
                        "((\d+|\.\d+)+(|\s+)/(|\s+)(\d+|\.\d+)+)|((\d+|\.\d+)+(|\s+)-(|\s+)(\d+|\.\d+)+)|((\d+|\.\d+)+(|\s+)x(|\s+)(\d+|\.\d+)+)|((\d+|\.\d+)+)",
                        input, re.IGNORECASE)
                    if unit:
                        unit = unit.group()
                    else:
                        unit = ""

                if (re.search(
                        "((\d+|\.\d+)+(|\s+)-(\d+|\.\d+)+(|\s+)/(|\s+)(\d+|\.\d+)+)|((\d+|\.\d+)+(|\s+)-(|\s+)(\d+|\.\d+)+)|((\d+|\.\d+)+(|\s+)x(|\s+)(\d+|\.\d+)+)|((\d+|\.\d+)+)|((\d+|\.\d+)+(|\s+)/(|\s+)(\d+|\.\d+)+)",
                        Description, re.IGNORECASE)):
                    uom = re.search(
                        "(L| L|L |fl oz | cu.ft.| sq.ft.|cu.ft.|sq.ft.| EA |EA |markers| markers|-markers|marker| marker|-marker|Meter(s)|-Meter(s)|Meter| Meter|-Meter|-Volt| Volt|mcg|-mcg| mcg|kg|-kg| kg|-G |G | g |g |-g |Each | each|EACH |each |Gummies| Gummies |gummies | gummies)",
                        input, re.IGNORECASE)
                    if uom:
                        uom = uom.group()
                    else:
                        uom = ""

        if (re.search(
                "((\d+|\.\d+)+(|\s+)(L| L|L |fl oz |-dozenglides|-glides| glides|glide|-glide| glide|L Short|L Long|L PETITE|L Tall|yds| yds|pc|-pc|pc| Sprays|Sprays|-Sprays|Spray| Spray|-Spray|XL| XL|-XL| ROLLS|-ROLLS|ROLLS| ROLL|-ROLL|ROLL| Piece(s)|-Piece(s)|Piece(s)| piece|-piece|piece| count|-count|count|/count |Each | each|EACH |each |Gummies| Gummies |gummies | gummies |pk| pk|Pk| Pk|Packets| Packets|packets| packets |Packet| Packet|packet| packet|Pan| Pan|pan| pan|Cups| Cups|cups| cups|Fl. Oz|-Fl. Oz.)(|\s+))|((\d+|\.\d+)+(|\s+)-(|\s+)(\d+|\.\d+)+(|\s+)(fl oz |glides|-glides| glides|glide|-glide| glide|L Short|L Long|L PETITE|L Tall|yds| yds|pc|-pc|pc| Sprays|Sprays|-Sprays|Spray| Spray|-Spray|XL| XL|-XL| ROLLS|-ROLLS|ROLLS| ROLL|-ROLL|ROLL| Piece(s)|-Piece(s)|Piece(s)| piece|-piece|piece| count|-count|count|/count |Each | each|EACH |each |Gummies| Gummies |gummies | gummies|pk| pk|Pk| Pk|Packets| Packets|packets| packets |Packet| Packet|packet| packet|Pan| Pan|pan| pan|Cups| Cups|cups| cups|Fl. Oz|-Fl. Oz.)(|\s+))|((\d+|\.\d+)+(|\s+)/(|\s+)(\d+|\.\d+)+(|\s+)(fl oz |glides|-glides| glides|glide|-glide| glide|L Short|L Long|L PETITE|L Tall|yds| yds|pc|-pc|pc| Sprays|Sprays|-Sprays|Spray| Spray|-Spray|XL| XL|-XL| ROLLS|-ROLLS|ROLLS| ROLL|-ROLL|ROLL| Piece(s)|-Piece(s)|Piece(s)| piece|-piece|piece| count|-count|count|/count |Each | each|EACH |each |Gummies| Gummies |gummies | gummies|pk| pk|Pk| Pk|Packets| Packets|packets| packets |Packet| Packet|packet| packet|Pan| Pan|pan| pan|Cups| Cups|cups| cups|Fl. Oz|-Fl. Oz.)(|\s+))|((\d+|\.\d+)+(|\s+)x(|\s+)(\d+|\.\d+)+(|\s+)(fl oz |glides|-glides| glides|glide|-glide| glide|L Short|L Long|L PETITE|L Tall|yds| yds|pc|-pc|pc| Sprays|Sprays|-Sprays|Spray| Spray|-Spray|XL| XL|-XL| ROLLS|-ROLLS|ROLLS| ROLL|-ROLL|ROLL| Piece(s)|-Piece(s)|Piece(s)| piece|-piece|piece| count|-count|count|/count |Each | each|EACH |each |Gummies| Gummies |gummies | gummies|pk| pk|Pk| Pk|Packets| Packets|packets| packets |Packet| Packet|packet| packet|Pan| Pan|pan| pan|Cups| Cups|cups| cups|Fl. Oz|-Fl. Oz.)(|\s+))",
                Description, re.IGNORECASE)):
            Size = re.search(
                "((\d+|\.\d+)+(|\s+)(fl oz |glides|-glides| glides|glide|-glide| glide|L Short|L Long|L PETITE|L Tall|yds| yds|pc|-pc|pc| Sprays|Sprays|-Sprays|Spray| Spray|-Spray|XL| XL|-XL| ROLLS|-ROLLS|ROLLS| ROLL|-ROLL|ROLL| Piece(s)|-Piece(s)|Piece(s)| piece|-piece|piece| count|-count|count|/count |Each | each|EACH |each |Gummies| Gummies |gummies | gummies|pk| pk|Pk| Pk|Packets| Packets|packets| packets |Packet| Packet|packet| packet|Pan| Pan|pan| pan|Cups| Cups|cups| cups|Fl. Oz|-Fl. Oz.)(|\s+))|((\d+|\.\d+)+(|\s+)-(|\s+)(\d+|\.\d+)+(|\s+)(fl oz |glides|-glides| glides|glide|-glide| glide|L Short|L Long|L PETITE|L Tall|yds| yds|pc|-pc|pc| Sprays|Sprays|-Sprays|Spray| Spray|-Spray|XL| XL|-XL| ROLLS|-ROLLS|ROLLS| ROLL|-ROLL|ROLL| Piece(s)|-Piece(s)|Piece(s)| piece|-piece|piece| count|-count|count|/count |Each | each|EACH |each |Gummies| Gummies |gummies | gummies|pk| pk|Pk| Pk|Packets| Packets|packets| packets |Packet| Packet|packet| packet|Pan| Pan|pan| pan|Cups| Cups|cups| cups|Fl. Oz|-Fl. Oz.)(|\s+))|((\d+|\.\d+)+(|\s+)-(|\s+)(\d+|\.\d+)+(|\s+)(fl oz |glides|-glides| glides|glide|-glide| glide|L Short|L Long|L PETITE|L Tall|yds| yds|pc|-pc|pc| Sprays|Sprays|-Sprays|Spray| Spray|-Spray|XL| XL|-XL| ROLLS|-ROLLS|ROLLS| ROLL|-ROLL|ROLL| Piece(s)|-Piece(s)|Piece(s)| piece|-piece|piece| count|-count|count|/count |Each | each|EACH |each |Gummies| Gummies |gummies | gummies|Packets| Packets|packets| packets |Packet| Packet|packet| packet|Pan| Pan|pan| pan|Cups| Cups|cups| cups|Fl. Oz|-Fl. Oz.)(|\s+))|((\d+|\.\d+)+(|\s+)/(|\s+)(\d+|\.\d+)+(|\s+)(fl oz |glides|-glides| glides|glide|-glide| glide|L Short|L Long|L PETITE|L Tall|yds| yds|pc|-pc|pc| Sprays|Sprays|-Sprays|Spray| Spray|-Spray|XL| XL|-XL| ROLLS|-ROLLS|ROLLS| ROLL|-ROLL|ROLL| Piece(s)|-Piece(s)|Piece(s)| piece|-piece|piece| count|-count|count|/count |Each | each|EACH |each |Gummies| Gummies |gummies | gummies|Packets| Packets|packets| packets |Packet| Packet|packet| packet|Pan| Pan|pan| pan|Fl. Oz|-Fl. Oz.)(|\s+))|((\d+|\.\d+)+(|\s+)/(|\s+)(\d+|\.\d+)+(|\s+)(fl oz |glides|-glides| glides|glide|-glide| glide|L Short|L Long|L PETITE|L Tall|yds| yds|pc|-pc|pc| Sprays|Sprays|-Sprays|Spray| Spray|-Spray|XL| XL|-XL| ROLLS|-ROLLS|ROLLS| ROLL|-ROLL|ROLL| Piece(s)|-Piece(s)|Piece(s)| piece|-piece|piece| count|-count|count|/count |Each | each|EACH |each |Gummies| Gummies |gummies | gummies|pk| pk|Pk| Pk|Packets| Packets|packets| packets |Packet| Packet|packet| packet|Pan| Pan|pan| pan|Fl. Oz|-Fl. Oz.)(|\s+))|((\d+|\.\d+)+(|\s+)-(|\s+)(\d+|\.\d+)+(|\s+)(fl oz |glides|-glides| glides|glide|-glide| glide|L Short|L Long|L PETITE|L Tall|yds| yds|pc|-pc|pc| Sprays|Sprays|-Sprays|Spray| Spray|-Spray|XL| XL|-XL| ROLLS|-ROLLS|ROLLS| ROLL|-ROLL|ROLL| Piece(s)|-Piece(s)|Piece(s)| piece|-piece|piece| count|-count|count |Count| Count|/count |Each | each|EACH |each |Gummies| Gummies |gummies | gummies|Packets| Packets|packets| packets |Packet| Packet|packet| packet|Pan| Pan|pan| pan|Cups| Cups|cups| cups|Fl. Oz|-Fl. Oz.)(|\s+))|((\d+|\.\d+)+(|\s+)/(|\s+)(\d+|\.\d+)+(|\s+)(glides|-glides| glides|glide|-glide| glide|L Short|L Long|L PETITE|L Tall|yds| yds|pc|-pc|pc| Sprays|Sprays|-Sprays|Spray| Spray|-Spray|XL| XL|-XL| ROLLS|-ROLLS|ROLLS| ROLL|-ROLL|ROLL| Piece(s)|-Piece(s)|Piece(s)| piece|-piece|piece| count|-count|count|/count |Count| Count |Each | each|EACH |each |Gummies| Gummies |gummies | gummies|Packets| Packets|packets| packets |Packet| Packet|packet| packet|Pan| Pan|pan| pan|Cups| Cups|cups| cups|Fl. Oz|-Fl. Oz.)(|\s+))|((\d+|\.\d+)+(|\s+)x(|\s+)(\d+|\.\d+)+(|\s+)(glides|-glides| glides|glide|-glide| glide|L Short|L Long|L PETITE|L Tall|yds| yds|pc|-pc|pc| Sprays|Sprays|-Sprays|Spray| Spray|-Spray|XL| XL|-XL| ROLLS|-ROLLS|ROLLS| ROLL|-ROLL|ROLL| Piece(s)|-Piece(s)|Piece(s)| piece|-piece|piece| count|-count|count|/count |Each | each|EACH |each |Gummies| Gummies |gummies | gummies|pk| pk|Pk| Pk|Packets| Packets|packets| packets |Packet| Packet|packet| packet|Pan| Pan|pan| pan|Cups| Cups|cups| cups|Fl. Oz|-Fl. Oz.)(|\s+))",
                Description, re.IGNORECASE)
            if Size:
                Size = Size.group()

        input = Description.lower()
        if re.search(
                "((\d+|\.\d+)+(|\s+)(L| L|L |pack-of|pack of - |pack of-|pack of |pack of|pack| pack|-pack|packs| packs|-packs|pk |-pk |-pk. |-pk. |Pk|Pc.| Pc.|pack of|pack|pk| pk|-pack)(|\s+))|((\d+|\.\d+)+(|\s+)-(|\s+)(\d+|\.\d+)+(|\s+)(Pack-of|Pack of - |pack of-|pack of |pack of|pack| pack|-pack|packs| packs|-packs|pk |-pk |-pk. |-pk.|Pc.| Pc. )(|\s+))|((\d+|\.\d+)+(|\s+)/(|\s+)(\d+|\.\d+)+(|\s+)(Pack-of|Pack of - |Pack of-|Pack of |Pack of|Pack| Pack|-Pack|Packs| Packs|-Packs|pk |-pk |-pk. |-pk.|Pc.| Pc. )(|\s+)|(pack of|pack of |Pack of - |pack of-|pack-of-)(\d+|\.\d+)+(|\s+))",
                input):
            input2 = re.search(
                "((\d+|\.\d+)+(|\s+)(L| L|L |pack-of|pack of - |pack of-|pack of |pack of|pack| pack|-pack|packs| packs|-packs|pk |-pk |-pk. |-pk. |pk|pc.| pc.|-pack)(|\s+))|((\d+|\.\d+)+(|\s+)-(|\s+)(\d+|\.\d+)+(|\s+)(pack-of|pack of - |pack of-|pack of |pack of|pack| pack|-pack|packs| packs|-packs|pk |-pk |-pk. |-pk.|Pc.| Pc. )(|\s+))|((\d+|\.\d+)+(|\s+)/(|\s+)(\d+|\.\d+)+(|\s+)(Pack-of|Pack of - |Pack of-|Pack of |Pack of|Pack| Pack|-Pack|Packs| Packs|-Packs|pk |-pk |-pk. |-pk.|Pc.| Pc. )(|\s+)|(pack of|pack of |Pack of - |pack of-|pack-of-)(\d+|\.\d+)+(|\s+))",
                input)
            if input2:
                input2 = input2.group()
            else:
                input2 = ""

            if re.search(
                    "((\d+|\.\d+)+(|\s+)-(|\s+)(\d+|\.\d+)+)|((\d+|\.\d+)+)|((\d+|\.\d+)+(|\s+)/(|\s+)(\d+|\.\d+)+)|(\d+|\.\d+)+(|\s+)",
                    input2):
                pack = re.search(
                    "((\d+|\.\d+)+(|\s+)-(|\s+)(\d+|\.\d+)+)|((\d+|\.\d+)+)|((\d+|\.\d+)+(|\s+)/(|\s+)(\d+|\.\d+)+)|(\d+|\.\d+)+(|\s+)",
                    input2)
                if pack:
                    pack = pack.group()
                else:
                    pack = ""

        if (pack == ""):
            pack = 1

        if (unit == "0" or unit == "0.0" or unit == "0.00" or unit == "000"):
            uom = ""
            unit = ""

        if (Size != "" and unit == "" and uom == ""):
            if re.search(
                    "((\\d+|\\.\\d+)+(|\\s+)/(|\\s+)(\\d+|\\.\\d+)+)|((\\d+|\\.\\d+)+(|\\s+)-(|\\s+)(\\d+|\\.\\d+)+)|((\\d+|\\.\\d+)+(|\\s+)x(|\\s+)(\\d+|\\.\\d+)+)|((\\d+|\\.\\d+)+)|((\\d+|\\.\\d+)+(|\\s+)/(|\\s+)(\\d+|\\.\\d+)+)",
                    Size, re.IGNORECASE):
                unit = re.search(
                    "((\\d+|\\.\\d+)+(|\\s+)/(|\\s+)(\\d+|\\.\\d+)+)|((\\d+|\\.\\d+)+(|\\s+)-(|\\s+)(\\d+|\\.\\d+)+)|((\\d+|\\.\\d+)+(|\\s+)x(|\\s+)(\\d+|\\.\\d+)+)|((\\d+|\\.\\d+)+)",
                    Size, re.IGNORECASE)
                if unit:
                    unit = unit.group()
                    uom = Size.replace(unit, "").strip().replace("-", "")
                else:
                    unit = ""

        if (uom.startswith('-')):
            uom = uom.split("-")[-1]

        if ('-' in unit):
            unit = unit.split("-")[-1]

        if (unit == "0" or unit == "0.0" or unit == "0.00" or unit == "000"):
            uom = ""
            unit = ""

        pack = str(pack).split('-')[-1].strip()

        uom = str(uom).strip()
        unit = str(unit).strip()
        pack = str(pack).strip()
        thisdict = {"pack": pack, "uom": uom, "unit": unit}
        return thisdict


#a=uom_uom_pack.get_unit_uom('1.5L')
#print(a)
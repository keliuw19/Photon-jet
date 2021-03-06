# This file was automatically created by FeynRules 2.3.36
# Mathematica version: 12.0.0 for Linux x86 (64-bit) (April 7, 2019)
# Date: Thu 17 Jun 2021 12:50:43



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
muSd = Parameter(name = 'muSd',
                 nature = 'external',
                 type = 'real',
                 value = 0.1,
                 texname = '\\text{muSd}',
                 lhablock = 'BSM',
                 lhacode = [ 1 ])

muAd = Parameter(name = 'muAd',
                 nature = 'external',
                 type = 'real',
                 value = 0.1,
                 texname = '\\text{muAd}',
                 lhablock = 'BSM',
                 lhacode = [ 2 ])

sh = Parameter(name = 'sh',
               nature = 'external',
               type = 'real',
               value = 0.001,
               texname = '\\text{sh}',
               lhablock = 'BSM',
               lhacode = [ 3 ])

d3pi = Parameter(name = 'd3pi',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = '\\text{d3pi}',
                 lhablock = 'BSM',
                 lhacode = [ 4 ])

CSdaa = Parameter(name = 'CSdaa',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{CSdaa}',
                  lhablock = 'BSM',
                  lhacode = [ 5 ])

CAdaa = Parameter(name = 'CAdaa',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{CAdaa}',
                  lhablock = 'BSM',
                  lhacode = [ 6 ])

CSd2pi = Parameter(name = 'CSd2pi',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{CSd2pi}',
                   lhablock = 'BSM',
                   lhacode = [ 7 ])

CAd3pi = Parameter(name = 'CAd3pi',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{CAd3pi}',
                   lhablock = 'BSM',
                   lhacode = [ 8 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

MSd = Parameter(name = 'MSd',
                nature = 'external',
                type = 'real',
                value = 1.,
                texname = '\\text{MSd}',
                lhablock = 'MASS',
                lhacode = [ 10001 ])

MAd = Parameter(name = 'MAd',
                nature = 'external',
                type = 'real',
                value = 1.,
                texname = '\\text{MAd}',
                lhablock = 'MASS',
                lhacode = [ 10002 ])

Mpi0 = Parameter(name = 'Mpi0',
                 nature = 'external',
                 type = 'real',
                 value = 0.1349766,
                 texname = '\\text{Mpi0}',
                 lhablock = 'MASS',
                 lhacode = [ 111 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00407,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

WSd = Parameter(name = 'WSd',
                nature = 'external',
                type = 'real',
                value = 0.00001,
                texname = '\\text{WSd}',
                lhablock = 'DECAY',
                lhacode = [ 10001 ])

WAd = Parameter(name = 'WAd',
                nature = 'external',
                type = 'real',
                value = 0.00001,
                texname = '\\text{WAd}',
                lhablock = 'DECAY',
                lhacode = [ 10002 ])

Wpi0 = Parameter(name = 'Wpi0',
                 nature = 'external',
                 type = 'real',
                 value = 7.82e-9,
                 texname = '\\text{Wpi0}',
                 lhablock = 'DECAY',
                 lhacode = [ 111 ])

Mpi = Parameter(name = 'Mpi',
                nature = 'internal',
                type = 'real',
                value = '0.137',
                texname = '\\text{Mpi}')

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

gpiaa = Parameter(name = 'gpiaa',
                  nature = 'internal',
                  type = 'real',
                  value = '1.7261924413437673*aEW',
                  texname = 'g_{\\text{piaa}}')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

AAd = Parameter(name = 'AAd',
                nature = 'internal',
                type = 'real',
                value = '(47*ee**2*(1 + MAd**6/(560.*MT**6) + MAd**4/(90.*MT**4) + MAd**2/(12.*MT**2)))/(48.*cmath.pi**2*vev)',
                texname = 'A_{\\text{Ad}}')

ASd = Parameter(name = 'ASd',
                nature = 'internal',
                type = 'real',
                value = '(47*ee**2*(1 - (2*MSd**4)/(987.*MT**4) - (14*MSd**2)/(705.*MT**2) + (213*MSd**12)/(2.634632e7*MW**12) + (5*MSd**10)/(119756.*MW**10) + (41*MSd**8)/(180950.*MW**8) + (87*MSd**6)/(65800.*MW**6) + (57*MSd**4)/(6580.*MW**4) + (33*MSd**2)/(470.*MW**2)))/(72.*cmath.pi**2*vev)',
                texname = 'A_{\\text{Sd}}')

GH = Parameter(name = 'GH',
               nature = 'internal',
               type = 'real',
               value = '-(G**2*(1 + (13*MH**6)/(16800.*MT**6) + MH**4/(168.*MT**4) + (7*MH**2)/(120.*MT**2)))/(12.*cmath.pi**2*vev)',
               texname = 'G_H')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*vev**2)',
                texname = '\\text{lam}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vev',
               texname = '\\text{yb}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')


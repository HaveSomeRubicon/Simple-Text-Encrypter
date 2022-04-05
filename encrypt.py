# ╔═╗░░░░░░╔╗░░░░░░░░░░░╔╗░░╔╗░░░░░░░░░░░░░░░░░░░░░
# ║╬╠╦╦═╦╦╦╝╠╗╔╦╗╔══╦═╗╔╝╠═╗║╚╦╦╗╔╗░░░░░░░░░░░░░░░░
# ║╔╣╔╣╬║║║╬║╚╣║║║║║║╬╚╣╬║╩╣║╬║║║╠╣░░░░░░░░░░░░░░░░
# ╚╝╚╝╚═╩═╩═╩═╬╗║╚╩╩╩══╩═╩═╝╚═╬╗║╚╝░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░╚═╝░░░░░░░░░░░░░╚═╝░░░░░░░░░░░░░░░░░░
# ╔╗░╔╗░░░░░░░░╔═══╗░░░░░░░░╔═══╗░░╔╗░░░░░░░░░░░╔╗░
# ║║░║║░░░░░░░░║╔═╗║░░░░░░░░║╔═╗║░░║║░░░░░░░░░░░║║░
# ║╚═╝╠══╦╗╔╦══╣╚══╦══╦╗╔╦══╣╚═╝╠╗╔╣╚═╦╦══╦══╦═╗║║░
# ║╔═╗║╔╗║╚╝║║═╬══╗║╔╗║╚╝║║═╣╔╗╔╣║║║╔╗╠╣╔═╣╔╗║╔╗╬╝░
# ║║░║║╔╗╠╗╔╣║═╣╚═╝║╚╝║║║║║═╣║║╚╣╚╝║╚╝║║╚═╣╚╝║║║╠╗░
# ╚╝░╚╩╝╚╝╚╝╚══╩═══╩══╩╩╩╩══╩╝╚═╩══╩══╩╩══╩══╩╝╚╩╝░
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# [['u^or', '5#:A', '7ntP', 'kh*k', 'Fsa.', "'C7$", 'tzqg', 'J&hT', '"<l`', 'e!x4', '^mof', '^3&y', 'O66O', 'Tw]x', "k'7!", 'Po1^', '`|Fz', '7pEV', 'TVYz', '8ntn', 'V=oO', 'Hgfj', '~<Uz', '<:8(', 'Cqb?', ']9@A', '>GF3', 'FVoc', 'ytmo', 'g^D.', 'wfp$', ':GTi', 'X-x9', ':%nI', '_Ah$', 'q6a(', 'Ln-E', 'uK*+', 'f3ne', "'ow%", 'Xtwx', '.yS)', '&erl', '[M&8', 'B^J[', 'SZT;', '`ZUM', '7]bC', 'QvK_', ',Fj5', '0wYL', 'ZU@y', '&;my', 'Mk6x', '|1Ew', '``Pc', '-0kM', '1%WA', 'ByWP', 'xja$', '6<*P', '~OE+', 'g!C,', 'Qt.-', 'aT=M', 'V|O]', 'Ok]*', ',iST', 'xt]e', 'V!,p', '|1|7', 'I98@', '`vqJ', 'Hbe&', 'nEZH', 'E>vW', 'qy:U', '`NAx', '2aNa', '[Er#', '`U0~', '>Mry', 'HfNg', '5(re', ',CAl', ')]wV', 'LBh_', 'jPw?', 'W&YH', "q-p'"], ['Kr<2', '%+iu', ':~Ap', "`'cs", 'F=>f', 'M>K(', 'U2L)', 'vfMO', 'y"VL', 'u<Fe', '[t)$', '[sT9', 'L,^F', 'enlt', '"!O!', 'czKf', '6gt!', "vL'C", 'L?zM', 'ua,G', '0uab', '2"iG', '_$g4', 'e$yE', 'd53~', '"\'r8', 'lb1^', 'iMBb', 'v!2&', '1XEc', ',Wfq', 'Y`tI', 'oJOF', '+OEj', 'V-,q', "'iUZ", 'et0y', '?q3O', '"bC;', 'e`(?', 'wrg(', 'RGX`', 'XQW.', 'PPv!', 'gL5x', "ST@'", 'h552', '?.~h', '~>Ut', 'z;oP', '+WV]', '"NQa', 'Bn+Z', 'l>#Q', 'pT_7', 'd3q`', '?u3c', 'Ruet', '^pZ!', 'R"d=', 'F*;P', '6v&A', 'D5sB', '&-Pk', '~JnA', "9y'[", '1WNu', '8fST', '+Qi6', '7KVP', '~=b0', ']^%6', 'ofn6', '=eu0', 'KyPj', "'EjE", '|50]', '+cN!', '+?$O', 'q)eI', 'O8*2', ')_UH', '`qtw', '2(%p', 'aCPK', '9Fp2', 'r+f5', 'CXkn', 'hNf<', '#.eC', 's>xp', '68W$', 'ye[r', '.T""', 'p6Y(', ',RIU', 'c$7n', ';<RS', '6df:', 'X:k]'], 4]
from cipher import chars
import random

def encrypt(text, cipher):
    main_key_raw = cipher[0]
    spices = cipher[1]
    length = cipher[2]
    
    # Make main key dictionary
    main_key = {}
    for key in main_key_raw:
        main_key[chars[main_key_raw.index(key)]] = key
    
    # Encrypt the text
    encrypted = ""
    for char in text:
        if random.randint(1,3) == 1:
            encrypted = encrypted + random.choice(spices)
            if random.randint(1,3) == 1:
                encrypted = encrypted + random.choice(spices)
                if random.randint(1,3) == 1:
                    encrypted = encrypted + random.choice(spices)
        try:
            encrypted = encrypted + main_key[char]
        except KeyError:
            print(f"EEROR: Unsupported character '{char}', the character will be skipped.")
    if random.randint(1,3) == 1:
            encrypted = encrypted + random.choice(spices)
            if random.randint(1,3) == 1:
                encrypted = encrypted + random.choice(spices)
                if random.randint(1,3) == 1:
                    encrypted = encrypted + random.choice(spices)
                    
    return encrypted
            
print(encrypt("Hello ÉÉÉworld", [['~2k1', 'p$IY', 'w3`j', ':&Xf', 'F%8U', 'X;Wc', 
                         'v+U.', '<v|j', '|1Ur', '~-1j', 'e0dO', 'vi|>', 
                         'Pe<)', 'Y1@a', 'A?Qf', '1@^R', 'h0M4', 'XK:!', 
                         'hGNk', 'Te8l', '?cNO', '?"4W', '&[!R', 'oNiz', 
                         '5v*3', '$gf+', 'w(g:', '+H6(', '`iS,', 'BScc', 
                         'wxV6', 'qoMo', '^a=t', '(Ayo', 'ec&]', 'LXsX', 
                         'SGQ^', '%~-k', "w1'P", 'F192', 'Unz~', 'F7<g', 
                         'PVh]', 'U8M*', '6Pmb', 'X@(O', 'SWO?', '3(@P', 
                         '&WHQ', 'kFMr', '|&sx', 'ZJBW', '^%(L', 'Rhn?', 
                         's$$:', 'VlsW', 'zCoM', 'xsKr', "q;L'", '_dD4', 
                         '][hw', ',weA', ']~G@', '+]Em', 'D2oE', '[$L#', 
                         '9Mn+', '-TcT', '1Y"Z', 'jSHg', 'h>QB', '_N#$', 
                         'e+TK', ']gF!', '#z;?', 'OSw#', 'Qz>Q', 'J>MG', 
                         '>;9Q', 'p@Ye', 'UP@?', '*Ru6', '#,`!', 'Gtjf', 
                         'LoFh', ']KJw', 'xyoq', 'g!uw', 'weB5', 'j67G'], 
                        ['o$1A', 'pg85', 'mO>4', 'o5I6', 'm.Bn', '5Nh(', 
                         'nD.w', '#T]6', 'KWpk', '!pJ"', 'cHOx', 'C0[`', 
                         'Mr?n', 'Tz(3', '&&ex', '+G+w', '3A:#', "Ji&'", 
                         'nBIy', 'utzo', 'Chw]', 'E]Ll', '_EPU', 'o%?6', 
                         '7"L>', 'a5C<', 'mWpt', 'gKb(', 'RLK&', 'Pfdr', 
                         '=2$P', 'Mk7m', '23+=', '?8s<', 'sE8a', 'OlZG', 
                         '9_90', 'L,2|', 'U;!.', 'i@6W', 'u=^(', '1HX,', 
                         '7ko3', '<SVB', 'LK3N', 'H5n8', '3WsL', 'p&v)', 
                         'h1pY', 'XB6k', 'U9xm', 'CXja', 'yO(a', ')8*6', 
                         '>~y1', '2*(X', 'ap]d', 'xaqw', 'ZzD3', 'dJ:h', 
                         's)1v', 'C85q', 'V#_)', '_=>*', 'v0P_', 'Zh]y', 
                         "fVi'", 'JQ>Q', 'F>zQ', 'lPaR', 'T.>7', 'GW~a', 
                         "0'L2", 'Ijs?', 'c56v', '?3,n', 'IffR', '-iGD', 
                         '.*k4', 'F*mV', 'q.WA', 'G2bO', 'sS%$', '+tHO', 
                         ')q47', 'mMCp', 'au2Y', 'G;43', '4ekV', '5[9D', 
                         '[^N4', 'n^Bl', '%)ko', '<~nr', 'LLTg', '927b', 
                         '"kD6', 'j2.Z', '&>Im', '@.ga'], 4]))
    
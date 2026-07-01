import pandas as pd
import numpy as np
 
linhas_completas = []
 
for n_dec in range(16):
    for t_dec in range(32):
        for u_dec in range(4):
            for v_dec in range(2):
                
                n3 = (n_dec >> 3) & 1
                n2 = (n_dec >> 2) & 1
                n1 = (n_dec >> 1) & 1
                n0 = (n_dec >> 0) & 1
                

                t4 = (t_dec >> 4) & 1
                t3 = (t_dec >> 3) & 1
                t2 = (t_dec >> 2) & 1
                t1 = (t_dec >> 1) & 1
                t0 = (t_dec >> 0) & 1
                

                u1 = (u_dec >> 1) & 1
                u0 = (u_dec >> 0) & 1
                

                v = v_dec
 

                comp_n_12 = 1 if n_dec >= 12 else 0
                

                comp_n_8 = 1 if n_dec >= 8 else 0
                

                comp_t_24 = 1 if t_dec >= 24 else 0
                

                iaf = u_dec + v
                

                iaf_4 = 1 if iaf == 4 else 0
                

                iaf_2 = 1 if iaf >= 2 else 0
 

                gatilho_flash_flood = 1 if (iaf_4 == 1 and comp_t_24 == 1) else 0
                

                vermelho = 1 if (comp_n_12 == 1 or gatilho_flash_flood == 1) else 0
                

                condicao_basal_amarelo = 1 if (comp_n_8 == 1 or iaf_2 == 1) else 0
                

                amarelo = 1 if (condicao_basal_amarelo == 1 and vermelho == 0) else 0
                

                alerta_verde = 1 if (vermelho == 0 and amarelo == 0) else 0
                

                if vermelho == 1:
                    status_led = "VERMELHO"
                elif amarelo == 1:
                    status_led = "AMARELO"
                else:
                    status_led = "VERDE"
                
 
                n_norm = n_dec / 15.0
                t_norm = t_dec / 31.0
                u_norm = u_dec / 3.0
                v_norm = float(v)
                IRE = (0.5 * n_norm) + (0.2 * u_norm) + (0.2 * v_norm) + (0.1 * t_norm)
                

                linhas_completas.append([
                    n_dec, f"{n3}{n2}{n1}{n0}",
                    t_dec, f"{t4}{t3}{t2}{t1}{t0}",
                    u_dec, f"{u1}{u0}",
                    v,
                    iaf,
                    round(IRE, 4),
                    status_led
                ])
 

colunas = [
    'N_Decimal', 'N_Binario(N3-N0)',
    'T_Decimal', 'T_Binario(T4-T0)',
    'U_Decimal', 'U_Binario(U1-U0)',
    'V_Bit',
    'IAF_Somador',
    'IRE_Teorico',
    'LED_Resultado'
]
 
df_completo = pd.DataFrame(linhas_completas, columns=colunas)
 

nome_arquivo = 'tabela_verdade_completa_4096.xlsx'
df_completo.to_excel(nome_arquivo, index=False)

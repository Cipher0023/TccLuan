import matplotlib.pyplot as plt
import pandas as pd

def plot_results(df):
    v_values = df['v_values']
    tc_values = df['tc_values']
    t1_values = df['t1_values']
    t2_values = df['t2_values']
    tt_values = df['tt_values']
    c1_values = df['c1_values']
    c2_values = df['c2_values']
    c3_values = df['c3_values']
    kp_values = df['kp_values']

    mintt = min(df['tt_values'])
    locxtt = v_values[df['tt_values'].idxmin()]
    minkp = min(df['kp_values'])
    locxkp = v_values[df['kp_values'].idxmin()]

    
    # Plotting curves
    plt.figure(1)
    plt.plot(v_values, tc_values,label='tc')
    plt.plot(v_values, t1_values,label='t1')
    plt.plot(v_values, t2_values,label='t2')
    plt.plot(v_values, tt_values,label='tt')
    plt.title('Curva de tempo', fontsize=18)
    plt.xlabel('v (m/min)', fontsize=14)
    plt.ylabel('min', fontsize=14)
    plt.legend(['tc', 't1', 't2', 'tt'])
    plt.ylim(0, 10)
    plt.savefig('figure1.png')  # Save figure1 to a file
    plt.close(1)  # Close figure1

    plt.figure(2)
    plt.plot(v_values, c1_values)
    plt.plot(v_values, c2_values)
    plt.plot(v_values, c3_values)
    plt.plot(v_values, kp_values)
    plt.title('Curva de custo', fontsize=18)
    plt.xlabel('v (m/min)', fontsize=14)
    plt.ylabel('R$/peça', fontsize=14)
    plt.legend(['c1', 'c2', 'c3', 'kp'])
    plt.savefig('figure2.png')  # Save figure2 to a file
    plt.close(2)  # Close figure2

    plt.figure(3)
    plt.plot(v_values, tt_values)
    plt.plot(v_values, kp_values)
    plt.scatter(locxtt, mintt, color='red', label='min tt', marker='o')
    plt.scatter(locxkp, minkp, color='blue', label='min kp', marker='o')
    plt.fill(
    [v_values.iloc[int(locxtt)], v_values.iloc[int(locxkp)], v_values.iloc[int(locxkp)], v_values.iloc[int(locxtt)]],
    [0, 0, minkp, minkp],
    color='white', alpha=0.0
    )


    plt.title('Curva do intervalo', fontsize=18)
    plt.xlabel('v (m/min)', fontsize=14)
    plt.ylabel('tempo e R$', fontsize=14)
    plt.legend(['tt', 'kp', 'minimo tt', 'minimo kt'])
    plt.savefig('figure3.png')  # Save figure3 to a file
    plt.close(3)  # Close figure3

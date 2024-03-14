import subprocess
import time

for i in range(2):
    for dim in [6, 12, 18, 24, 30]:
        gpu = 0
        subprocess.run(['screen', 'python','/content/Finite-expression-method/fex/Schrodinger/controller_cubic_sh_firstdeflation_thenintegral.py', '--epoch', '1000', '--bs', '10', '--greedy', '0.1', '--gpu', '0', '--ckpt', 'Firstdeflat_thenintegral_epoch1k_Dim'+str(dim), '--tree', 'depth2_sub', '--random_step', '3', '--lr', '0.002','--dim', str(dim), '--base', '200000', '--left', '-1', '--right', '1', '--domainbs', '2000', '--intbs', '10000'])
        print('running dim '+str(dim))
        time.sleep(100)

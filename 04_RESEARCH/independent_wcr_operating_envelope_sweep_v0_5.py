import numpy as np
import pandas as pd

def wrap(x):
    return (x + np.pi) % (2*np.pi) - np.pi

def run(q0, phi0, rho, kappa, K, nonlinear, coupling, noise, steps=120, P=1.0, seed=0):
    rng = np.random.default_rng(seed)
    q, phi, a = q0, phi0, 0j
    rows = []
    for _ in range(steps):
        I = abs(a)**2
        qn = np.clip(rho*q + nonlinear*np.tanh(I-1.0) + coupling*np.sin(phi) + rng.normal(0, noise), -1, 1)
        phin = wrap(phi + 0.5*nonlinear*np.tanh(I-1.0) + 0.8*coupling*q + rng.normal(0, noise))
        a = rho*a + kappa/(1 + 1j*K*qn)*np.exp(1j*phin)
        q, phi = qn, phin
        rows.append((q, phi, abs(a)))
    return np.asarray(rows)

rows = []
for rho in [0.80, 0.90, 0.97, 0.995]:
    for coupling in [0.02, 0.10, 0.20, 0.40]:
        for nonlinear in [0.02, 0.08, 0.20, 0.40]:
            for noise in [0.0, 0.01, 0.05, 0.10, 0.20]:
                A = run(0.20, 0.0, rho, 0.26, 3.0, nonlinear, coupling, noise, seed=1)
                B = run(0.20, np.pi, rho, 0.26, 3.0, nonlinear, coupling, noise, seed=2)
                ya, yb = A[-30:,2].mean(), B[-30:,2].mean()
                contrast = abs(ya-yb)/(0.5*(ya+yb)+1e-12)
                sep = np.mean(np.sqrt((A[-30:,0]-B[-30:,0])**2 + wrap(A[-30:,1]-B[-30:,1])**2))
                bounded = max(np.max(np.abs(A[:,0])), np.max(np.abs(B[:,0]))) <= 1.000001 and max(np.max(A[:,2]), np.max(B[:,2])) < 100
                rows.append([rho,coupling,nonlinear,noise,contrast,sep,bounded])

df = pd.DataFrame(rows, columns=["rho","coupling","nonlinear","noise","output_contrast","state_separation","bounded"])
df.to_csv("wcr_operating_envelope_v0_5_results.csv", index=False)
df["gate_pass"] = (df.output_contrast > 0.10) & (df.state_separation > 0.5) & df.bounded
robust = df[df.noise <= 0.10].groupby(["rho","coupling","nonlinear"])["gate_pass"].mean().reset_index()
print(robust[robust.gate_pass >= 0.80].to_string(index=False))

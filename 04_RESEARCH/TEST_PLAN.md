# RESEARCH TEST PLAN

## First mathematical test

X = [1,2]^T
A = [[2,1],[-1,3]]
Expected Y = [4,5]^T

Error:
epsilon = ||Y_physical - Y_ideal|| / ||Y_ideal||

## Progressive scaling

2x2 -> 4x4 -> 8x8 -> 16x16 -> 32x32

## Error injection

1. ideal
2. propagation loss
3. phase error
4. timing jitter
5. amplitude noise
6. combined errors

## Measurements

accuracy
latency
energy
area estimate
noise tolerance
state reuse ratio
communication overhead
correction overhead

## Energy accounting

laser/source
encoding
modulation
propagation
nonlinear device
memory
detector
control
correction

## Comparison

Bandingkan dengan equivalent digital implementation setelah physical overhead lengkap.

## Scaling criterion

Desain yang bekerja pada 2x2 tetapi overhead energi/control tumbuh lebih cepat daripada useful computation tidak dianggap scalable.

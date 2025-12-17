import matplotlib.pyplot as plt

high_threshold = 10
low_threshold = 8

throughput_high = [i * 0.1 for i in range(70, 110)]
throughput_low = list(reversed(throughput_high))

sampling_high = [10 if t <= high_threshold else 2 for t in throughput_high]
sampling_low = [2 if t >= low_threshold else 10 for t in throughput_low]

plt.figure()
plt.plot(throughput_high, sampling_high, label="Increasing throughput")
plt.plot(throughput_low, sampling_low, label="Decreasing throughput")
plt.xlabel("Throughput (Mbps)")
plt.ylabel("Sampling Interval (seconds)")
plt.title("Hysteresis Loop for SDN Controller Sampling")
plt.legend()
plt.grid(True)
plt.show()

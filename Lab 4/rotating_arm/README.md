# Runaway Snack：Rotating Arm 第一轮测试

代码位置：`Interactive-Lab-Hub` 仓库的 `Fall2026` 分支，`Lab 4/rotating_arm/`。

已由用户终端输出确认：Raspberry Pi 5 Model B Rev 1.1、Debian 12 Bookworm、Python 3.11.2，存在 `/dev/i2c-1`。这仅确认系统和总线接口存在，尚未确认外设通信。

Pi 当前安装 miniPiTFT 小屏幕；安装 pHAT 前先关机断电并处理接口占用，不可将 pHAT 错位插在剩余针脚上。

本轮已确认照片中的 Hitec HS-318 和 Miuzei MS18，以及双轴 SG90 云台结构。
推荐先用 HS-318 做竖直轴、水平摆动的短臂。照片不能验证舵机是否完好。
已确认驱动板为 SparkFun Servo pHAT DEV-15316；不必另购 PCA9685 板。供电状态和 Raspberry Pi OS 环境仍待确认。
提供 sensor_test.py 和 rotating_arm.py，先按顺序测试，确认供电后才能运行舵机程序。

## 结构

- 底座建议从约 15 × 15 cm 的硬纸板/小盒子起步，加固并配重。
- HS-318 输出轴朝上，机身固定在底座上；通过安装耳固定，不要仅靠一块胶带。
- 使用照片中原装的黑色舵盘，以中心螺丝锁紧；短臂连接到舵盘上，不粘到裸轴上。
- 轴心到托盘中心先做 8–10 cm；托盘直径约 4–5 cm。这是试做尺寸，不是额定承重指标。
- 调试顺序：舵机空载、小范围运动 → 短臂 → 空托盘 → 纸球/轻零食。
- 先通过程序居中，断开舵机电源，再安装舵盘和臂。装好后先小范围试转，不要手拧输出轴或直接扫满行程。
- 传感器固定在托盘原位前方或旁边的小支架上，感应面朝向手，且处于手伸来的高度。
- 传感器不要随臂移动，也不要被托盘、纸板、胶带遮挡。
- 若长臂明显下垂或轴摇晃，先缩短、减重；需要承载更重物品时加独立转轴/轴承支撑。

## 只连接 APDS-9960

先给 Pi 关机、断电，再接线。下表只适用于用户链接的 Adafruit APDS-9960 breakout。
编号是 40 针接口的物理针脚编号，并非 BCM GPIO 编号。

| APDS-9960 | Raspberry Pi 5 |
|---|---|
| VIN | 3.3V，物理针脚 1 |
| GND | GND，物理针脚 6 |
| SDA | GPIO2/SDA1，物理针脚 3 |
| SCL | GPIO3/SCL1，物理针脚 5 |

INT、3Vo 暂时不接。如果 Pi 上已经有 HAT/pHAT，不要为了接线硬插或错位叠板；先确认板的型号及可用接口。
有标准 Qwiic/STEMMA QT 接口时可以用兼容线缆连接；检查端口标签，不要只按线色判断。

## 在 Raspberry Pi 上运行，不能在 Mac 上直接读取这块传感器

如果课程已有可以正常读取 I2C 传感器的 Python 虚拟环境，优先沿用它。
如果没有，可在 Raspberry Pi OS 上准备：

```bash
sudo raspi-config
```

在 Interface Options 中启用 I2C；若系统提示重启，先重启。

```bash
sudo apt update
sudo apt install -y python3-venv python3-pip python3-lgpio i2c-tools
cd ~/Interactive-Lab-Hub/"Lab 4"
# 已有 .venv 时直接激活，不必重新创建。
python3 -m venv --system-site-packages .venv
source .venv/bin/activate
python -m pip install -r rotating_arm/requirements.txt
cd rotating_arm
i2cdetect -y 1
```

传感器通常应看到地址 `39`；正确连接并供电的 Servo pHAT 应看到 `40`。`70` 也可能出现，是 PCA9685 的 All Call 地址。
若缺少对应地址，先断电检查供电、SDA/SCL、焊接或线缆，不要继续装机械结构。
确认 Pi 上的仓库已同步这些文件，在 Lab 4/rotating_arm 目录运行：

```bash
python sensor_test.py
```

记录没有手、手靠近预期触发位置、手离开时的读数。也检查托盘在两个位置时会不会被误认成手。
读数是 0–255 的反射红外强度，不是厘米；实际可用范围和手、环境、安装方式有关。
如果无手与有手读数重叠，先改位置，不能只靠换阈值解决。

## 已确认的 Servo pHAT 接法与供电条件

DEV-15316 用 PCA9685 芯片，I2C 地址是 0x40。本程序使用 Adafruit PCA9685 驱动访问这块 SparkFun 板，不需要再买板，也不需要同时运行 SparkFun 示例。
所有其他舵机先拔掉，仅使用通道 0。关闭其他正在控制 pHAT 的程序，因为它们会相互覆盖输出。

断电安装 pHAT，40 针插座须完整对齐，留出 Pi 5 散热器和风扇空间。
APDS-9960 有 STEMMA QT 插座时，可用 Qwiic/STEMMA QT 兼容 4 针线接到 pHAT 的 Qwiic 插座。
HS-318 的信号线（通常黄线）接通道 0 信号针，红线接 5V，黑线/棕线接 GND；以板的丝印和舵机线序为准，不凭插头朝向猜测。

**供电必须先确认：** DEV-15316 的 Power Isolation 跳线默认闭合，pHAT 的舵机电源与 Pi 的 5V 相连。此时不能把两个独立 5V 电源当作互相隔离的电源直接使用。

长期带载建议使用官方支持的分开供电方式：断电后正确断开 Power Isolation 跳线并检查隔离，Pi 5 用自己的合适电源，pHAT USB-C 用独立稳压 5V 电源（只带一个 HS-318 可从 5V/2A 起步），两板通过 GPIO 共地。不要改动 Fuse Bypass 跳线。
目前尚未检查用户实物跳线和电源。先拍板背面和电源标签核对；若不熟悉切断跳线，可让实验室助教协助。

不修改跳线的替代方法是：pHAT USB-C 留空、从 Pi 获取板自身电源；通过三线转接让舵机红线只接外部稳压 5V，舵机地接外部负极并与 pHAT GND 共地，舵机信号接通道 0。**舵机红线不得同时接 pHAT 的 5V 针，外部正极也不得接 Pi 5V。** 这需要能把三根线分别转接的线材。

不要用长臂把舵机顶在机械限位上。出现卡住、持续嗡鸣、明显发热时断开舵机电源检查。

## 舵机程序：确认供电后，在 Pi 上运行

先卸下长臂；首次启动会把舵机移到名义中位。

```bash
python rotating_arm.py center
```

中位保持期间，先断开舵机电源，再用 Ctrl+C 结束程序并安装舵盘。不要在保持通电时强扭轴来对齐。
再次启动仍可能有运动；手离开运动范围。

```bash
python rotating_arm.py sweep
```

默认 1400–1600 微秒仅用于保守的小范围测试，不代表 60°。先空载测试，再逐步加短臂、空托盘和轻载。
需要更大范围时，每次向外扩展约 50 微秒，并观察实际角度及是否卡住；程序限制在 1000–2000 微秒内，但这不保证任意装配结构都不会碰撞。程序数值不代替真实角度校准。

集成运行必须填写测得的阈值。以下 80/40 **仅演示命令格式**，应换成你现场确定的值：

```bash
python rotating_arm.py run --near 80 --far 40
```

也可把已经机械测试过的两个位置传进去，例如：

```bash
python rotating_arm.py run --near 80 --far 40 --rest-us 1300 --escape-us 1700
```

程序在退出时停止 PWM，不自动归位；此时舵机不再主动保持位置，断开电源前托住容易下垂的结构。
此脚本只适用于普通位置舵机，不适用于经过改装的连续旋转舵机。

目标逻辑：连续约 0.1 秒超过触发阈值 → 用约 0.4–0.6 秒转开 → 保持；连续约 1 秒低于释放阈值 → 用约 0.8–1 秒返回。
释放阈值应低于触发阈值，中间区间保持原状态。时间是第一轮试调建议。
传感器只能判断自己的检测区是否清空，不能判断整张桌子上是否还有手。
转角先小后大，最终目标可约 45–60°；API 数值角度不一定等于真实物理角度。

## 官方参考

- [APDS-9960 Python 使用](https://learn.adafruit.com/adafruit-apds9960-breakout/circuitpython)
- [APDS-9960 API / proximity 含义](https://docs.circuitpython.org/projects/apds9960/en/latest/api.html)
- [Blinka 与 Raspberry Pi 安装](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi)
- [HS-318 规格](https://hitecrcd.com/hs-318-standard-voltage-resin-gear-25t-analog-sport-servo/)
- [PCA9685 接线和 Python](https://learn.adafruit.com/16-channel-pwm-servo-driver/python-circuitpython)
- [SparkFun Servo pHAT v2](https://learn.sparkfun.com/tutorials/pi-servo-phat-v2-hookup-guide/all)

程序已做语法检查，并检查触发确认、阈值滞回和释放等待逻辑；尚未连接用户实物测试。传感器阈值、舵机有效行程和承载能力均需要在实物上测定。

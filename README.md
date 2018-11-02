Leap api (quantum computing cloud environment) programming samples.
===

# Overview

These files are sample codes using Leap.
[Leap](https://cloud.dwavesys.com/leap/login/?next=/leap/) is the cloud environment of quantum computing (annealing) provided by D-Wave. Almost sample codes are taken from [D-Wave Ocean Software Documentaion](https://docs.ocean.dwavesys.com/en/latest/index.html)

## Dependency

python 2.7

## Setup

1. Create your account at [D-Wave Leap](https://cloud.dwavesys.com/leap/login/).

2. After login, you can get `API TOKEN` and `Solver API endpoint`. Those two are required to use sample codes.

3. Read [Installing Ocean Tools](https://docs.ocean.dwavesys.com/en/latest/overview/install.html) and build the environment.

4. Read [Confiuring a D-Wave System as a Solver](https://docs.ocean.dwavesys.com/en/latest/overview/dwavesys.html#configuring-a-d-wave-system-as-a-solver) and configure the solver.

5. Rename the file config/account.py.default as config/account.py.Then edit the constant `LEAP_API_TOKEN` like below.

  ```
  LEAP_API_TOKEN='YOUR_API TOKEN'
  ```

　Additioinally, rename the file config/config.py.default to config/config.py.<br>
　Then edit the constant `API_ENDPOINT` and `SOLVER_NAME` like below.

  ```
  API_ENDPOINT='YOUR_API_ENDPOINT'
  SOLVER_NAME='YOUR_SOLVER_NAME'
  ```

　You can decide 'SOLVER_NAME' as you like.

6. Then, you can execute python codes in the `sample` directory.

## Usage

Just execute python code like below.

```
$ python sample/019vetex_cover/021wheel_graph_dwave.py
```

In the sample directory, the name of direcoties and python files consist of 3 digits number and name of directory or file. The 3 digit number represents the referenced page of [D-Wave Ocean Software Documentaion](https://docs.ocean.dwavesys.com/en/latest/index.html)

So, please check the 3 digit number of the name and read the correspondent page of documentaion if you know about the codes.

#!/bin/bash

pushd ./bpftrace; ./build.sh; popd;
pushd ./ftrace; ./build.sh; popd;
pushd ./netm; ./build.sh; popd;
pushd ./perf; ./build.sh; popd;
pushd ./sysc; ./build.sh; popd;
pushd ./sysm; ./build.sh; popd;

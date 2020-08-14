#!/bin/bash

echo "Creating image pi.png and writing report to run.out."

circos -conf pi.conf -debug_group summary,timer > run.out

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Ornl 1
# GNU Radio version: 3.8.1.0

from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation


class ornl_1(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Ornl 1")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_magphase_to_complex_1 = blocks.magphase_to_complex(1)
        self.blocks_magphase_to_complex_0 = blocks.magphase_to_complex(1)
        self.blocks_head_0 = blocks.head(gr.sizeof_gr_complex*1, 50*samp_rate)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, 'ornl_1.bin', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_complex_to_magphase_0 = blocks.complex_to_magphase(1)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)
        self.blocks_complex_to_arg_0 = blocks.complex_to_arg(1)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, 1, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_complex_to_arg_0, 0), (self.blocks_magphase_to_complex_1, 1))
        self.connect((self.blocks_complex_to_mag_0, 0), (self.blocks_magphase_to_complex_1, 0))
        self.connect((self.blocks_complex_to_magphase_0, 1), (self.blocks_magphase_to_complex_0, 1))
        self.connect((self.blocks_complex_to_magphase_0, 0), (self.blocks_magphase_to_complex_0, 0))
        self.connect((self.blocks_head_0, 0), (self.blocks_complex_to_magphase_0, 0))
        self.connect((self.blocks_magphase_to_complex_0, 0), (self.blocks_complex_to_arg_0, 0))
        self.connect((self.blocks_magphase_to_complex_0, 0), (self.blocks_complex_to_mag_0, 0))
        self.connect((self.blocks_magphase_to_complex_1, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_head_0, 0))


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_head_0.set_length(50*self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)





def main(top_block_cls=ornl_1, options=None):
    tb = top_block_cls()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    tb.start()

    tb.wait()


if __name__ == '__main__':
    main()

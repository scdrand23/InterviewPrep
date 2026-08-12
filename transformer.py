# %%

import torch.nn as nn
import torch 


class PositionalEncoding(nn.Module):


    def __init__(self, seq_length, d_model, device):

        super(PositionalEncoding, self).__init__()

        self.pos_enc = torch.zeros(seq_length, d_model, device=device, requires_grad=False)

        pos = torch.arange(0, seq_length, dtype=torch.float).unsqueeze(1)

        _2i = torch.arange(0, d_model, step=2, device=device).float()

        self.pos_enc[:, 0::2] = torch.sin(pos / (10000 ** (_2i / d_model)))
        self.pos_enc[:, 1::2] = torch.cos(pos / (10000 ** (_2i / d_model)))

    def forward(self, x):
        batch_size, seq_length = x.size()
        return self.pos_enc[:seq_length, :]





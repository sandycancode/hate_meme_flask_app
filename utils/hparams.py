hparams = { 
    # Optional hparams
    "embedding_dim": 768,
    "language_feature_dim": 768,
    "vision_feature_dim": 768,
    "fusion_output_size": 256,
    "dev_limit": None,
    "lr": 0.00005,
    "max_epochs": 10,
    "n_gpu": 0,
    "batch_size": 8,
    # allows us to "simulate" having larger batches 
    "accumulate_grad_batches": 16,
    "early_stop_patience": 3
}
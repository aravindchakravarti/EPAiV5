# EPAiV5-Session28
Session-28 Optimizing Neural Network

# Result:
Achieved 2.5x speed compared to original unoptimized model. Unoptimzed model takes roughly 350ms, where as optimized model takes 140ms. Which is close to 2.5x.
Logs are below

Otimization techniques used:
1. model.compile
2. autocast
3. `data.to(device, non_blocking=True)`
4. input data/images to FP16 from FP32

# Logs
## Without optimization
```
Loss=1.8440531492233276 Batch_id=24 Accuracy=20.10: 100%|██████████| 25/25 [00:22<00:00,  1.12it/s] --> EPOCH: 0, Avg Time Taken = 364.24ms
Test set: Average loss: 2.3147, Accuracy: 1018/10000 (10.18%)

Loss=1.5698350667953491 Batch_id=24 Accuracy=36.91: 100%|██████████| 25/25 [00:17<00:00,  1.40it/s] --> EPOCH: 1, Avg Time Taken = 345.98ms
Test set: Average loss: 1.6351, Accuracy: 4002/10000 (40.02%)

Loss=1.3989874124526978 Batch_id=24 Accuracy=45.71: 100%|██████████| 25/25 [00:16<00:00,  1.54it/s] --> EPOCH: 2, Avg Time Taken = 351.46ms
Test set: Average loss: 1.4153, Accuracy: 4768/10000 (47.68%)

Loss=1.2505789995193481 Batch_id=24 Accuracy=51.70: 100%|██████████| 25/25 [00:17<00:00,  1.45it/s] --> EPOCH: 3, Avg Time Taken = 353.29ms
Test set: Average loss: 1.3094, Accuracy: 5279/10000 (52.79%)

Loss=1.1860575675964355 Batch_id=24 Accuracy=56.12: 100%|██████████| 25/25 [00:17<00:00,  1.44it/s] --> EPOCH: 4, Avg Time Taken = 349.37ms
Test set: Average loss: 1.2343, Accuracy: 5523/10000 (55.23%)
```

## With optimization
```
Loss=1.9019148349761963 Batch_idx=24 Accuracy=19.70: 100%|██████████| 25/25 [00:44<00:00,  1.78s/it] --> EPOCH: 1, Avg Time Taken = 1375.91ms
Test set: Average loss: 2.3237, Accuracy: 1000/10000 (10.00%)

Loss=1.487034797668457 Batch_idx=24 Accuracy=37.28: 100%|██████████| 25/25 [00:17<00:00,  1.45it/s] --> EPOCH: 2, Avg Time Taken = 141.22ms
Test set: Average loss: 1.5923, Accuracy: 4166/10000 (41.66%)

Loss=1.409718632698059 Batch_idx=24 Accuracy=45.82: 100%|██████████| 25/25 [00:16<00:00,  1.51it/s] --> EPOCH: 3, Avg Time Taken = 140.07ms
Test set: Average loss: 1.4568, Accuracy: 4739/10000 (47.39%)

Loss=1.314367651939392 Batch_idx=24 Accuracy=51.11: 100%|██████████| 25/25 [00:16<00:00,  1.51it/s] --> EPOCH: 4, Avg Time Taken = 140.72ms
Test set: Average loss: 1.3476, Accuracy: 5141/10000 (51.41%)

Loss=1.1803094148635864 Batch_idx=24 Accuracy=54.78: 100%|██████████| 25/25 [00:16<00:00,  1.52it/s] --> EPOCH: 5, Avg Time Taken = 140.00ms
Test set: Average loss: 1.2401, Accuracy: 5487/10000 (54.87%)
```
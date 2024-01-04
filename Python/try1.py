import numpy as numpy

class NeuralNetwork:
    # ...

    def train(self, input_vectors, targets, iterations):
        cumulative_errors = []
        for current_iteration in range(iterations):
            # Pick a data instance at random
            random_data_index = np.random.randint(len(input_vectors))

            input_vector = input_vectors[random_data_index]
            target = targets[random_data_index]

            # Compute the gradients and update the weights
            derror_dbias, derror_dweights = self._compute_gradients(
                input_vector, target
            )

            self._update_parameters(derror_dbias, derror_dweights)

            # Measure the cumulative error for all the instances
            if current_iteration % 100 == 0:
                cumulative_error = 0
                # Loop through all the instances to measure the error
                for data_instance_index in range(len(input_vectors)):
                    data_point = input_vectors[data_instance_index]
                    target = targets[data_instance_index]

                    prediction = self.predict(data_point)
                    error = np.square(prediction - target)

                    cumulative_error = cumulative_error + error
                cumulative_errors.append(cumulative_error)

        return cumulative_errors


In [45]: # Paste the NeuralNetwork class code here
   ...: # (and don't forget to add the train method to the class)

In [46]: import matplotlib.pyplot as plt

In [47]: input_vectors = np.array(
   ...:     [
   ...:         [3, 1.5],
   ...:         [2, 1],
   ...:         [4, 1.5],
   ...:         [3, 4],
   ...:         [3.5, 0.5],
   ...:         [2, 0.5],
   ...:         [5.5, 1],
   ...:         [1, 1],
   ...:     ]
   ...: )

targets = np.array([0, 1, 0, 1, 0, 1, 1, 0])

learning_rate = 0.1

neural_network = NeuralNetwork(learning_rate)

worst_error = 0
best_error = 999999999

training_error = neural_network.train(input_vectors, targets, 10000)

for

#plt.plot(training_error)
#In [53]: plt.xlabel("Iterations")
#In [54]: plt.ylabel("Error for all training instances")
#In [54]: plt.savefig("cumulative_error.png")

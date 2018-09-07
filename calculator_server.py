# -*- coding: utf-8 -*-

from concurrent import futures
import time

import grpc

import calculator_pb2
import calculator_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

import calculator

class Calculator(calculator_pb2_grpc.CalculatorServicer):
    def AddAB(self, request, context):
	response = calculator_pb2.NumberResponse()
	response.value = calculator.add_ab(request.a,request.b)
	return response
    def MulAB(self, request, context):
	response = calculator_pb2.NumberResponse()
	response.value = calculator.mul_ab(request.a,request.b)
	return response

def serve():
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
	calculator_pb2_grpc.add_CalculatorServicer_to_server(Calculator(), server)
	server.add_insecure_port('[::]:50052')
	server.start()
	try:
		while True:
			time.sleep(_ONE_DAY_IN_SECONDS)
	except KeyboardInterrupt:
		server.stop(0)

if __name__ == '__main__':
    serve()

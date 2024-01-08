FROM public.ecr.aws/lambda/python:3.12
COPY calculator.py ${LAMBDA_TASK_ROOT}
CMD [ "calculator.lambda_handler" ]
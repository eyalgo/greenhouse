from opentelemetry import trace
from opentelemetry.sdk.resources import SERVICE_NAME, OTELResourceDetector, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

DEFAULT_SERVICE_NAME = "agent-with-manual-instrumentation"

# Resource.create applies the attributes it is given after the environment's, so handing it the
# default directly would mask OTEL_SERVICE_NAME and OTEL_RESOURCE_ATTRIBUTES. Take the name the
# environment resolves (an empty value counts as unset) and fall back to the default only when
# the environment names none.
service_name = OTELResourceDetector().detect().attributes.get(SERVICE_NAME) or DEFAULT_SERVICE_NAME

provider = TracerProvider(resource=Resource.create({SERVICE_NAME: service_name}))
exporter = OTLPSpanExporter(insecure=True)
processor = BatchSpanProcessor(exporter)
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

tracer = trace.get_tracer("agent-tracer")

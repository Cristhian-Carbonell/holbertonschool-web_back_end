export default function guardrail(mathFunction) {
  const elements = [];
  const message = 'Guardrail was processed';
  try {
    const value = mathFunction();
    if (Number.isInteger(value)) {
      elements.push(value);
    }
  } catch (ex) {
    const error = `Error: ${ex.message}`;
    elements.push(error);
  }
  elements.push(message);

  return elements;
}

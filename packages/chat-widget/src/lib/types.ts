export interface Message {
  role: 'user' | 'assistant';
  content: string;
  /** Whether this message is still being "typed" onto the screen */
  typing?: boolean;
}

export interface ChatWidgetProps {
  /** Lambda Function URL */
  apiUrl: string;
  /** Header title shown in the panel */
  title?: string;
  /** Input placeholder text */
  placeholder?: string;
}

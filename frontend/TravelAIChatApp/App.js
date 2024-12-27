import React, { useState, useEffect } from 'react';
import { View, TextInput, Button, StyleSheet } from 'react-native';
import { GiftedChat } from 'react-native-gifted-chat';
import { SafeAreaProvider } from 'react-native-safe-area-context';

const App = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false); // Loading state

  // Initialize the chat with a welcome message
  useEffect(() => {
    setMessages([
      {
        _id: 1,
        text: 'Hello, I am Travel.AI. How can I help you?',
        createdAt: new Date(),
        user: {
          _id: 2,
          name: 'Travel.AI',
          avatar: 'https://placeimg.com/140/140/tech',
        },
      },
    ]);
  }, []);

  const fetchResponse = async (url, userQuery, chatHistory) => {
    setIsLoading(true);
    try {
      const response = await fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          user_query: userQuery,
          chat_history: chatHistory,
        }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const contentType = response.headers.get('content-type');
      let data;

      if (contentType && contentType.includes('application/json')) {
        data = await response.json();
      } else {
        const text = await response.text();
        try {
          if (text[0] === '[' || text[0] === '{') {
            data = JSON.parse(text);
          } else {
            data = [];
          }
        } catch (error) {
          console.error('Error parsing JSON:', error);
          return;
        }
      }

      return data;
    } catch (error) {
      console.error('Error fetching response from API:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const handleSend = async () => {
    if (input.trim()) {
      // Add user message to chat
      const userMessage = {
        _id: Math.round(Math.random() * 1000000),
        text: input,
        createdAt: new Date(),
        user: {
          _id: 1,
          name: 'You',
        },
      };

      setMessages((previousMessages) => GiftedChat.append(previousMessages, userMessage));
      setInput('');

      try {
        const chatHistory = messages.map((msg) => ({
          type: msg.user._id === 1 ? 'Human' : 'AI',
          content: msg.text,
        }));

        const data = await fetchResponse('http://192.168.8.104:5000/get_response', input, chatHistory);

        if (data?.response) {
          // Add AI's response to the chat
          const aiMessage = {
            _id: Math.round(Math.random() * 1000000),
            text: data.response,
            createdAt: new Date(),
            user: {
              _id: 2,
              name: 'Travel.AI',
            },
          };

          setMessages((previousMessages) => GiftedChat.append(previousMessages, aiMessage));
        }
      } catch (error) {
        console.error('Error processing API response:', error);
      }
    }
  };

  return (
    <SafeAreaProvider>
      <View style={styles.container}>
        <GiftedChat
          messages={messages}
          onSend={() => handleSend()}
          user={{
            _id: 1,
          }}
          renderInputToolbar={() => (
            <View style={styles.inputToolbar}>
              <TextInput
                style={styles.input}
                value={input}
                onChangeText={setInput}
                placeholder="Type your message..."
              />
              <Button title={isLoading ? 'Sending...' : 'Send'} onPress={handleSend} disabled={isLoading} />
            </View>
          )}
        />
      </View>
    </SafeAreaProvider>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
  },
  inputToolbar: {
    flexDirection: 'row',
    alignItems: 'center',
    padding: 10,
    backgroundColor: '#fff',
    borderTopWidth: 1,
    borderTopColor: '#ccc',
  },
  input: {
    flex: 1,
    borderColor: '#ccc',
    borderWidth: 1,
    borderRadius: 20,
    padding: 10,
    marginRight: 10,
  },
});

export default App;
